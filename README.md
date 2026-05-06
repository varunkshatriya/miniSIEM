# 🔐 MiniSIEM - Log Analyzer & Threat Detector

MiniSIEM is a beginner-friendly **Security Information and Event Management (SIEM)** tool built using Python. It analyzes system logs to detect suspicious activities such as brute force attacks.

---

## 🚀 Features

* 🔍 Detects multiple failed login attempts
* ⚠️ Identifies brute force attacks (count-based detection)
* ⏱️ Detects time-based attacks (within 30 seconds)
* 🌐 Tracks and displays suspicious IP addresses
* 🔄 Generates dynamic logs to simulate real-world attacks

---

## 🛠️ Tech Stack

* Python
* Collections
* Datetime

---

## 📁 Project Structure

```
MiniSIEM/
 ├── logs/
 │    └── sample.log
 ├── siem.py
 ├── log_generator.py
 ├── rules.py
 ├── README.md
```

---

## ▶️ How to Run

### 1. Generate logs

```bash
python log_generator.py
```

### 2. Run the SIEM analyzer

```bash
python siem.py
```

---

## 📊 Sample Output

```
--- Analysis Report ---

[ALERT] Brute force attack (count) from IP: 192.168.1.10
[ALERT] Brute force attack (time-based) from IP: 192.168.1.10
192.168.1.10 → 7 failed attempts

Top suspicious IP: 192.168.1.10
```

---

## 🎯 What this project demonstrates

* Log parsing and analysis
* Basic cybersecurity threat detection
* Python-based system design
* Simulation of real-world attack scenarios

---

## 🚀 Future Improvements

* Real-time log monitoring
* Web-based dashboard (Flask)
* Email/SMS alerts
* Integration with cloud logs

---

## 👨‍💻 Author

Varun Kshatriya
