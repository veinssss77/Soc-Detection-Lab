# Incident Investigation: SSH Brute Force Attack

## Scenario
A server shows multiple failed SSH login attempts in a short period.

## Objective
Determine if this is a brute-force attack and identify the attacker.

---

## Log Analysis

From the logs:

- Multiple "Failed password" entries detected
- IP: 192.168.1.10 attempted login 4 times rapidly
- Another IP (192.168.1.30) attempted only once

---

## Findings

- 192.168.1.10 exceeded threshold (3 attempts)
- Pattern indicates automated brute-force attack
- Attack targeted "root" account

---

## Detection Method

A Python script was used to:
- Parse log entries
- Count failed login attempts per IP
- Flag suspicious behavior based on threshold

---

## Conclusion

- Confirmed brute-force attack from 192.168.1.10
- Recommended:
  - Block IP using firewall
  - Disable root login
  - Implement fail2ban

---

## Skills Demonstrated

- Log analysis
- Threat detection
- Python for security automation
- Incident reporting
