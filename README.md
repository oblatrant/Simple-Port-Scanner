# 🔍 Simple Python Port Scanner

Beginner-friendly **Port scanner** written in Python.
Designed for educational and authorized security testing only, this tool scans a user-specified port range on a target host and reports all open ports.

---

## Features

* Scans any host by IP or hostname
* Configurable port range (`--start` / `--end`)
* Adjustable timeout for connection attempts
* Clean, readable code (great for learning)
* Optional threaded scanning supported in commented code

---

## How It Works

The scanner attempts to create a TCP connection to each port in the selected range:

* If the connection succeeds → **port is open**
* If it times out or refuses → **port is closed**

This uses Python’s built-in `socket` module.
---

## Usage

### **Run the scanner**

```bash
python3 port_scanner.py <target>
```

### **Scan a custom range**

```bash
python3 port_scanner.py 192.168.1.10 --start 1 --end 65535
```

### **Adjust timeout**

```bash
python3 port_scanner.py scanme.nmap.org --timeout 1.5
```

---

## Example Output

```
[*] Scanning host: scanme.nmap.org
[*] Port range:    1–1024
[*] Start time:    2025-01-14 12:30:55

[+] Port 22 is open
[+] Port 80 is open

[*] Scan complete at 2025-01-14 12:31:10
```

---


## Requirements

* Python **3.x**

---



