
# SOC Detection Lab – SSH Brute Force Attack

## Overview
This project simulates a real-world cybersecurity scenario where a server is targeted by a brute-force SSH attack.

The objective is to detect malicious activity using log analysis and basic automation.

---

## Project Structure

- logs/auth.log → Simulated system logs
- scripts/detect_bruteforce.py → Detection script
- analysis/investigation.md → Incident report

---

## Attack Scenario

An attacker repeatedly attempts to log into the server via SSH using different credentials.

---

## Detection Approach

- Parsed system logs
- Identified failed login attempts
- Counted attempts per IP
- Flagged suspicious IPs exceeding threshold

---

## Results

- Detected brute-force attack from 192.168.1.10
- Generated alert using Python script

---

## Skills Demonstrated

- Security log analysis
- Threat detection
- Python scripting
- Basic incident response

---

## Future Improvements

- Integrate with SIEM tools like Splunk
- Real-time monitoring
- Automated IP blocking
