# 🖥️ System Health Monitoring Script

This Python script provides system health monitoring capabilities with email reporting functionality. It allows users to check various system metrics and receive email reports about system health.

## ✨ Features

### 1. Disk Usage Monitoring 💾
- Function: `check_disk_usage()`
- Monitors disk space utilization using psutil
- Returns percentage of disk usage and total disk space in GB
- Handles exceptions and returns error messages if monitoring fails

### 2. Running Services Monitor 🔄
- Function: `monitor_running_services()`
- Lists all currently running system services using systemctl
- Uses OS commands to fetch service status
- Returns formatted list of active services
- Includes error handling for command execution failures

### 3. Memory Usage Assessment 🧮
- Function: `assess_memory_usage()`
- Tracks system memory utilization using psutil
- Provides memory usage percentage and total available memory in GB
- Includes exception handling for monitoring failures

### 4. CPU Usage Evaluation ⚡
- Function: `evaluate_cpu_usage()`
- Monitors CPU utilization percentage
- Uses psutil with 1-second interval for accurate measurement
- Returns current CPU usage percentage
- Handles potential monitoring errors

### 5. Email Reporting System 📧
- Function: `send_email_report()`
- Compiles system health metrics into a comprehensive report
- Sends email using SMTP (Gmail)
- Includes all monitored metrics in the email body
- Features secure email authentication
- Handles email sending failures with error reporting

## 📋 Interactive Menu
The script includes an interactive menu system that allows users to:
- Choose specific monitoring functions
- Execute individual checks
- Send complete system reports via email
- Exit the program

## ⚠️ Error Handling
- Comprehensive exception handling throughout all functions
- User-friendly error messages
- Graceful error recovery

## 📌 Requirements
- Python 3.x
- psutil library
- Access to SMTP server (Gmail)
- System permissions for service monitoring

## 🚀 Usage
Run the script and follow the interactive menu prompts:
1. Select options 1-4 for individual system checks
2. Choose option 5 to send an email report
3. Select option 6 to exit the program

## 📝 Note
Email configuration requires valid Gmail credentials and may need app-specific password for authentication.

## 🔧 About psutil Library
The script heavily relies on psutil (Python System and Process Utilities), which is a cross-platform library for retrieving information on running processes and system utilization. Here's what psutil provides:

### System Resources Monitoring
- **CPU Statistics**: 
  - Per-CPU and system-wide CPU utilization
  - CPU frequency
  - CPU count (physical and logical)
  - CPU time spent in different modes (user, system, idle)

### Memory Information
- **Virtual Memory**: 
  - Total and available memory
  - Used and free memory
  - Memory usage percentage
  - Swap memory statistics

### Disk Management
- **Storage Information**:
  - Partitions and disk usage
  - Disk I/O statistics
  - Read/write counts and bytes
  - Disk latency information

### Network Statistics
- **Network Interfaces**:
  - Network connections (TCP/UDP)
  - Network interface cards statistics
  - Network I/O counters

### Process Management
- **Process Information**:
  - Process list and status
  - Process CPU usage
  - Process memory usage
  - Open files and connections

### Cross-Platform Compatibility
- Works consistently across:
  - Linux
  - Windows
  - macOS
  - FreeBSD
  - OpenBSD
  - NetBSD
  - Sun Solaris

### Installation

```bash
pip install psutil
```

