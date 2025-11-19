
By the end of **Module 1 (Weeks 1–4)**, your students have covered:

* **Week 1:** Variables, input/output, data types
* **Week 2:** Conditional logic and `if` statements
* **Week 3:** Lists and basic data structures
* **Week 4:** Loops and iteration

They now have the fundamentals to write small, functional scripts that can perform meaningful cybersecurity-related automation tasks.

Below is a **Module 1 Homework Assignment** that’s structured like a *mini-project*: it’s realistic, tests all key concepts, and reinforces cybersecurity thinking without being overly technical.

---

# 🧩 **Module 1 Homework: Python Scripting Fundamentals – “Security Log Classifier”**

### **Assignment Theme:**

**Write a Python script that analyzes login events and reports security insights.**

---

## **Scenario**

You’ve just joined the Security Operations Center (SOC) as a junior analyst.
Your supervisor gives you a small text log containing a week’s worth of login activity from different systems.
Each line in the file contains a **username**, an **IP address**, and a **login result** (`SUCCESS` or `FAILURE`).

Your task is to write a Python script that:

1. Reads and stores this log data,
2. Identifies patterns of failed logins,
3. Classifies IP addresses as internal or external,
4. Prints a short summary report of activity.

---

## **Sample Log (provided to students as `logins.txt`)**
There should be a logins.txt in your workspace that vaguely resembles this structure.
```
alice 192.168.1.15 SUCCESS
bob 8.8.8.8 FAILURE
charlie 10.0.0.12 SUCCESS
bob 8.8.8.8 FAILURE
dave 172.16.0.5 FAILURE
alice 192.168.1.15 SUCCESS
bob 8.8.8.8 FAILURE
eve 10.1.2.3 SUCCESS
```

---

## **Your Script Should:**

### **1️⃣ Read the Data (Week 1 Concepts)**

* Open the file and read all lines.
* Print a message confirming how many login records were found.

```python
with open("logins.txt") as f:
    lines = f.readlines()

print(f"Loaded {len(lines)} login records.")
```

---

### **2️⃣ Store Data in Lists (Week 3 Concepts)**

* Create a list for each field (e.g., `users`, `ips`, `results`) **or** store each log line as a list of parts.

```python
for line in lines:
    parts = line.strip().split()
    # parts = [username, ip, result]
```

---

### **3️⃣ Use Conditional Logic (Week 2 Concepts)**

* Identify **failed** logins using `if` statements.
* Count how many failed vs. successful attempts occurred overall.

```python
if parts[2] == "FAILURE":
    failed_logins += 1
else:
    successful_logins += 1
```

---

### **4️⃣ Use Loops to Classify IPs (Week 4 Concepts)**

Loop through all IP addresses and determine whether they are **internal** (start with `10.` or `192.168.`) or **external**.

Add counters for each type.

---

### **5️⃣ Output a Summary Report**

Print a clean, readable summary like:

```
Total login attempts: 8
Successful logins: 3
Failed logins: 5
Internal IPs: 4
External IPs: 4

Possible brute-force alert:
User 'bob' had 3 failed logins from IP 8.8.8.8
```

---

## **Stretch Goals (Optional for Bonus Credit)**

* ✅ Detect users with **3 or more failed logins** and print a warning for each.
* ✅ Write your summary output to a new file (`summary.txt`).
* ✅ Ask the user for the log filename as input instead of hardcoding it.

---

## **Deliverables**

Students should submit:

1. Their Python script (`security_log_classifier.py`)
2. Screenshot or copy of program output
3. (Optional) `summary.txt` if they implemented file output

---

## **Evaluation Rubric (50 points total)**

| Category                      | Points | Criteria                                          |
| ----------------------------- | ------ | ------------------------------------------------- |
| File reading and data parsing | 10     | Successfully loads and reads log file             |
| Use of conditionals           | 10     | Correctly identifies failed and successful logins |
| Use of lists and iteration    | 10     | Stores and processes multiple log entries         |
| Output formatting / summary   | 10     | Provides readable, accurate report                |
| Code readability and comments | 10     | Includes comments and clear structure             |

**Bonus (+5)**: Detects multiple failed logins from the same user or IP.
**Bonus (+5)**: Writes summary to file.

---

## **Instructor Notes**

This assignment reinforces:

* **Practical automation thinking:** working with repetitive log data
* **Scripting confidence:** reading files, looping, classifying
* **Security mindset:** pattern recognition and anomaly detection

🧠 **Suggested Classroom Wrap-up Discussion:**

* “Why might repeated failed logins be suspicious?”
* “How could this script scale up for a real SOC tool?”
* “What new Python skill would make this script even better?” (→ dictionaries or file writing in Module 2)
