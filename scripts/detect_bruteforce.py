# This script analyzes SSH logs to detect brute-force attacks

# Path to the log file
log_file = "../logs/auth.log"

# Dictionary to store failed attempts per IP
failed_attempts = {}

# Threshold: how many failed attempts = suspicious
THRESHOLD = 3

# Open and read the log file
with open(log_file, "r") as file:
    for line in file:

        # Check if the line indicates a failed login
        if "Failed password" in line:

            # Extract IP address (last part of the line)
            parts = line.split()
            ip = parts[-4]  # IP is located near end

            # Count attempts per IP
            if ip not in failed_attempts:
                failed_attempts[ip] = 0

            failed_attempts[ip] += 1

# Analyze results
print("=== Brute Force Detection Results ===\n")

for ip, count in failed_attempts.items():
    print(f"{ip} -> {count} failed attempts")

    # If attempts exceed threshold → alert
    if count >= THRESHOLD:
        print(f"[ALERT] Possible brute-force attack from {ip}\n")
