# Automated System Health Check Cron Job

## Overview
The purpose of the cron job is to automate the execution of a system health check script at regular intervals, specifically every 4 hours. This automation ensures that the system is continuously monitored without requiring manual intervention.

## Key Health Checks Performed
- **Disk Usage**: Monitors disk space to ensure the system is not running out of storage
- **Running Services**: Checks if essential services are active and running
- **Memory Usage**: Assesses the memory consumption of the system to prevent overuse  
- **CPU Usage**: Evaluates CPU load to ensure the system is not being overloaded
- **Email Report**: Sends a comprehensive report summarizing the results of these checks to the designated email

## Benefits
By scheduling this cron job, system administrators can ensure high availability and reliability by proactively monitoring system health.


