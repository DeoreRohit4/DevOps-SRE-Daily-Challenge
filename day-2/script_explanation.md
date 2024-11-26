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
```
import json
from datetime import datetime, timedelta
```
