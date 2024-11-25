import os
import psutil  # For system monitoring
import smtplib
from email.mime.text import MIMEText
from time import sleep

def check_disk_usage():
    try:
        usage = psutil.disk_usage('/')
        return f"Disk Usage: {usage.percent}% used out of {usage.total / (1024 ** 3):.2f} GB"
    except Exception as e:
        return f"Error checking disk usage: {e}"

def monitor_running_services():
    try:
        services = os.popen('systemctl list-units --type=service --state=running').read()
        return f"Running Services:\n{services}"
    except Exception as e:
        return f"Error fetching running services: {e}"

def assess_memory_usage():
    try:
        memory = psutil.virtual_memory()
        return f"Memory Usage: {memory.percent}% used of {memory.total / (1024 ** 3):.2f} GB"
    except Exception as e:
        return f"Error checking memory usage: {e}"

def evaluate_cpu_usage():
    try:
        cpu_usage = psutil.cpu_percent(interval=1)
        return f"CPU Usage: {cpu_usage}%"
    except Exception as e:
        return f"Error checking CPU usage: {e}"

def send_email_report():
    try:
        sender = "rohitdeore114@gmail.com"
        recipient = "deorerohit31@gmail.com"
        subject = "System Health Report"
        body = f"""
        {check_disk_usage()}
        {assess_memory_usage()}
        {evaluate_cpu_usage()}
        {monitor_running_services()}
        """
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = recipient

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender, 'slzwylspkbkmfxee')
            server.send_message(msg)
        return "Email report sent successfully."
    except Exception as e:
        return f"Error sending email: {e}"

def menu():
    print("\nSystem Health Check Menu")
    print("1. Check Disk Usage")
    print("2. Monitor Running Services")
    print("3. Assess Memory Usage")
    print("4. Evaluate CPU Usage")
    print("5. Send Email Report")
    print("6. Exit")

if __name__ == "__main__":
    while True:
        menu()
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                print(check_disk_usage())
            elif choice == 2:
                print(monitor_running_services())
            elif choice == 3:
                print(assess_memory_usage())
            elif choice == 4:
                print(evaluate_cpu_usage())
            elif choice == 5:
                print(send_email_report())
            elif choice == 6:
                print("Exiting script. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")

