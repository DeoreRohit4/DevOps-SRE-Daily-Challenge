# Detailed Documentation of the Python Script
## 1. Script Objective
The script analyzes and optimizes Amazon S3 bucket metadata from a JSON file, focusing on:
- Summarizing bucket details.
- Identifying large and unused buckets.
- Calculating storage costs grouped by region and department.
- Recommending cleanup or archival actions for cost savings.

## 2. Prerequisites
- Python 3 installed on your system.
- JSON file (buckets.json) containing S3 bucket metadata.

## 3. Step-by-Step Explanation
Importing Libraries
```python
import json
from datetime import datetime, timedelta
```
- `json`: To parse the JSON file containing bucket metadata.
- `datetime`: For date manipulation to calculate the age of each bucket.

## Loading and Parsing JSON
```python
with open("buckets.json", "r") as file:
    data = json.load(file)

buckets = data["buckets"]
```
- Opens buckets.json in read mode.
- Loads the JSON data into a Python dictionary.
- Extracts the buckets list, which contains metadata for each bucket.

## Constants
```python
today = datetime.today()
unused_days_threshold = 90
delete_unused_days_threshold = 20
cleanup_size_threshold = 50
delete_size_threshold = 100
s3_cost_per_gb = 0.023  # Example cost per GB
glacier_cost_per_gb = 0.004  # Example cost for Glacier
```
- `today`: Captures the current date for date-based calculations.
- Thresholds:
  - `unused_days_threshold`: Defines unused duration for identifying idle buckets (>90 days).
  - `delete_unused_days_threshold`: Specifies the deletion threshold for large unused buckets (>20 days).
  - `cleanup_size_threshold`: Size above which cleanup is recommended (>50 GB).
  - `delete_size_threshold`: Size above which unused buckets are queued for deletion (>100 GB).
- Costs:
  - `s3_cost_per_gb`: Example cost per GB of S3 storage.
  - `glacier_cost_per_gb`: Example cost per GB for archival to Glacier.

## Helper Function: Days Since Creation
```python
def days_since_creation(created_on):
    return (today - datetime.strptime(created_on, "%Y-%m-%d")).days
```
- Converts the bucket's createdOn date string to a datetime object.
- Computes the number of days between the creation date and today.

## Task 1: Printing a Bucket Summary
```python
print("Bucket Summary:")
for bucket in buckets:
    print(f"Name: {bucket['name']}, Region: {bucket['region']}, "
          f"Size: {bucket['sizeGB']} GB, Versioning: {bucket['versioning']}")
```
- Iterates over each bucket in the JSON data.
- Prints key details:
  - `name`: Name of the bucket.
  - `region`: AWS region.
  - `sizeGB`: Size in GB.
  - `versioning`: Whether versioning is enabled.

## Task 2: Identify Large and Unused Buckets
```python
print("\nBuckets Larger Than 80 GB and Unused for 90+ Days:")
unused_buckets = []
for bucket in buckets:
    if bucket['sizeGB'] > 80 and days_since_creation(bucket['createdOn']) > unused_days_threshold:
        unused_buckets.append(bucket)
        print(f"Name: {bucket['name']}, Region: {bucket['region']}, "
              f"Size: {bucket['sizeGB']} GB, Days Unused: {days_since_creation(bucket['createdOn'])}")
```
- Filters buckets:
  - Size greater than 80 GB (`bucket['sizeGB'] > 80`).
  - Unused for over 90 days (`days_since_creation(bucket['createdOn']) > unused_days_threshold`).
- Appends such buckets to `unused_buckets`.
- Prints the name, region, size, and unused duration for each bucket.

## Task 3: Cost Report
Initialization
```python
region_department_cost = {}
deletion_queue = []
```
- region_department_cost: Dictionary to store costs grouped by region and department.
- deletion_queue: List to hold buckets identified for deletion.

Processing Buckets
```python
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
```
- Calculates the cost of each bucket (cost = bucket['sizeGB'] * s3_cost_per_gb).
- Organizes costs by region and department.
- Adds buckets to:
  - deletion_queue if size >100 GB and unused for 20+ days.
  - Cleanup recommendations if size >50 GB.

Printing Costs
```python
for region, departments in region_department_cost.items():
    print(f"Region: {region}")
    for department, cost in departments.items():
        print(f"  Department: {department}, Total Cost: ${cost:.2f}")
```
- Iterates through region_department_cost to display total costs grouped by region and department.

## Task 4: Final Deletion and Archival Suggestions
Deletion Queue
```python
print("\nDeletion Queue (Buckets to Delete):")
for bucket in deletion_queue:
    print(f"Name: {bucket['name']}, Region: {bucket['region']}, Size: {bucket['sizeGB']} GB")
```
- Lists buckets in `deletion_queue`.

Archival Suggestions
```python
print("\nBuckets Suggested for Archival to Glacier:")
for bucket in buckets:
    if bucket not in deletion_queue and bucket['sizeGB'] > cleanup_size_threshold:
        print(f"Name: {bucket['name']}, Region: {bucket['region']}, Size: {bucket['sizeGB']} GB")
```
- Identifies large buckets (>50 GB) not in the deletion queue as candidates for archival to Glacier.

## 4. Output Example
Here’s how the script outputs:
```yaml
Bucket Summary:
Name: prod-data, Region: us-west-2, Size: 120 GB, Versioning: True
...

Buckets Larger Than 80 GB and Unused for 90+ Days:
Name: old-backups, Region: us-east-2, Size: 200 GB, Days Unused: 1198
...

Cost Report:
Region: us-west-2
  Department: analytics, Total Cost: $2.76
...

Deletion Queue (Buckets to Delete):
Name: old-backups, Region: us-east-2, Size: 200 GB

Buckets Suggested for Archival to Glacier:
Name: compliance-data, Region: ca-central-1, Size: 300 GB
```

## 5. Challenges and Key Learnings
- Challenges:
  - Handling edge cases (e.g., missing metadata).
  - Balancing multiple thresholds and conditions.

- Learnings:
  - Automating resource cleanup enhances cost efficiency.
  - JSON processing and date calculations are crucial for cloud management scripts.

# Thank you!
