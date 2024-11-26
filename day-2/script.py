import json
from datetime import datetime, timedelta

# Load the JSON data
with open("buckets.json", "r") as file:
    data = json.load(file)

buckets = data["buckets"]

# Constants
today = datetime.today()
unused_days_threshold = 90
delete_unused_days_threshold = 20
cleanup_size_threshold = 50
delete_size_threshold = 100
s3_cost_per_gb = 0.023  # Example cost per GB
glacier_cost_per_gb = 0.004  # Example cost for Glacier

# Helper functions
def days_since_creation(created_on):
    return (today - datetime.strptime(created_on, "%Y-%m-%d")).days

# Task 1: Print a summary of each bucket
print("Bucket Summary:")
for bucket in buckets:
    print(f"Name: {bucket['name']}, Region: {bucket['region']}, "
          f"Size: {bucket['sizeGB']} GB, Versioning: {bucket['versioning']}")

# Task 2: Identify buckets larger than 80 GB unused for 90+ days
print("\nBuckets Larger Than 80 GB and Unused for 90+ Days:")
unused_buckets = []
for bucket in buckets:
    if bucket['sizeGB'] > 80 and days_since_creation(bucket['createdOn']) > unused_days_threshold:
        unused_buckets.append(bucket)
        print(f"Name: {bucket['name']}, Region: {bucket['region']}, "
              f"Size: {bucket['sizeGB']} GB, Days Unused: {days_since_creation(bucket['createdOn'])}")

# Task 3: Generate a cost report
print("\nCost Report:")
region_department_cost = {}
deletion_queue = []
for bucket in buckets:
    region = bucket['region']
    department = bucket['tags'].get('team', 'unknown')
    cost = bucket['sizeGB'] * s3_cost_per_gb
    region_department_cost.setdefault(region, {}).setdefault(department, 0)
    region_department_cost[region][department] += cost

    # Recommendations based on size
    if bucket['sizeGB'] > delete_size_threshold and days_since_creation(bucket['createdOn']) > delete_unused_days_threshold:
        deletion_queue.append(bucket)
    elif bucket['sizeGB'] > cleanup_size_threshold:
        print(f"Bucket '{bucket['name']}' in {region} (Size: {bucket['sizeGB']} GB) - Recommend Cleanup.")

for region, departments in region_department_cost.items():
    print(f"Region: {region}")
    for department, cost in departments.items():
        print(f"  Department: {department}, Total Cost: ${cost:.2f}")

# Task 4: Final deletion list and Glacier suggestion
print("\nDeletion Queue (Buckets to Delete):")
for bucket in deletion_queue:
    print(f"Name: {bucket['name']}, Region: {bucket['region']}, Size: {bucket['sizeGB']} GB")

print("\nBuckets Suggested for Archival to Glacier:")
for bucket in buckets:
    if bucket not in deletion_queue and bucket['sizeGB'] > cleanup_size_threshold:
        print(f"Name: {bucket['name']}, Region: {bucket['region']}, Size: {bucket['sizeGB']} GB")
