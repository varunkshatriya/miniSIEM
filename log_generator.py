import random
from datetime import datetime, timedelta

ips = ["192.168.1.10", "192.168.1.20", "10.0.0.5"]
statuses = ["LOGIN FAILED", "LOGIN SUCCESS"]

start_time = datetime.now()

with open("logs/sample.log", "w") as file:
    for i in range(20):
        time = start_time + timedelta(seconds=i * random.randint(1, 5))
        ip = random.choice(ips)

        # Increase probability of failed attempts for one IP (simulate attack)
        if ip == "192.168.1.10":
            status = "LOGIN FAILED"
        else:
            status = random.choice(statuses)

        log = f"{time.strftime('%Y-%m-%d %H:%M:%S')} {status} IP:{ip}\n"
        file.write(log)

print("Logs generated successfully!")