#This python script will generate real time system utilization report for cpu,memory,harddisk
import psutil
import openpyxl

# Create a new Excel workbook
workbook = openpyxl.Workbook()
sheet = workbook.active

# Write headers
sheet["A1"] = "CPU (%)"
sheet["B1"] = "Memory (%)"
sheet["C1"] = "Disk Usage (%)"

# Get system information
cpu_percent = psutil.cpu_percent()
memory_percent = psutil.virtual_memory().percent
disk_usage = psutil.disk_usage('/').percent

# Write system information to the Excel sheet
sheet["A2"] = cpu_percent
sheet["B2"] = memory_percent
sheet["C2"] = disk_usage

# Save the Excel workbook
workbook.save("system_report.xlsx")
