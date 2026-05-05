from collections import defaultdict
from datetime import datetime

log_file = "logs/sample.log"

ip_attempts = defaultdict(int)
ip_timestamps = defaultdict(list)

# Read log file
with open(log_file, "r") as file:
    for line in file:
        if "FAILED" in line:
            timestamp = datetime.strptime(line[:19], "%Y-%m-%d %H:%M:%S")
            ip = line.split("IP:")[1].strip()

            ip_attempts[ip] += 1
            ip_timestamps[ip].append(timestamp)

print("\n--- Analysis Report ---\n")

# 🔥 Brute force detection (count-based)
for ip, count in ip_attempts.items():
    if count >= 5:
        print(f"[ALERT] Brute force attack (count) from IP: {ip}")

# 🔥 Time-based detection (real SIEM logic)
for ip, times in ip_timestamps.items():
    times.sort()
    for i in range(len(times) - 4):
        diff = (times[i + 4] - times[i]).seconds
        if diff <= 30:
            print(f"[ALERT] Brute force attack (time-based) from IP: {ip}")
            break

# Show attempts
for ip, count in ip_attempts.items():
    print(f"{ip} → {count} failed attempts")

# Top suspicious IP
if ip_attempts:
    top_ip = max(ip_attempts, key=ip_attempts.get)
    print(f"\nTop suspicious IP: {top_ip}")