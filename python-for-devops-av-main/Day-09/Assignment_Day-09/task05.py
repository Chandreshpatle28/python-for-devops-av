# DevOps script to analyze log files for errors

# Sample log file data
log_file = [
    "INFO: Process started",
    "ERROR: Null pointer exception",
    "INFO: Process completed",
    "WARNING: Disk space low",
    "ERROR: Connection timeout"
]

# Loop through log entries and identify errors
for entry in log_file:
    if "ERROR" in entry:
        print(f"Error detected: {entry}")

# Alternative: Using a while loop with break
# index = 0
# while index < len(log_file):
#     if "ERROR" in log_file[index]:
#         print(f"Error detected: {log_file[index]}")
#         break
#     index += 1