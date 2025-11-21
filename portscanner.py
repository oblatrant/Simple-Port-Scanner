#!/usr/bin/env python3
#
# Simple Port Scanner (for authorized use only!)
# Author: <your name>
#
# This script checks which TCP ports are open on a target system.
# It is intentionally minimal, readable, and beginner-friendly.
#

import socket
import argparse
from datetime import datetime

# import threading
# import queue


def scan_port(host: str, port: int, timeout: float = 0.5) -> bool:
    """
    Attempt to connect to a TCP port.
    Returns True if the port is open, otherwise False.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        try:
            sock.connect((host, port))
            return True
        except (socket.timeout, ConnectionRefusedError, OSError):
            return False

# def worker_thread(host: str, q: "queue.Queue[int]"):
#     """Thread worker: scans ports pulled from a queue."""
#     while not q.empty():
#         port = q.get()
#         if scan_port(host, port):
#             print(f"[+] Port {port} is open")
#         q.task_done()



def main():
    # Argument parsing
    parser = argparse.ArgumentParser(
        description="Simple Python port scanner (authorized testing only)"
    )

    parser.add_argument("host", help="Target hostname or IP address")
    parser.add_argument("--start", type=int, default=1, help="Start of port range")
    parser.add_argument("--end", type=int, default=1024, help="End of port range")
    parser.add_argument(
        "--timeout", type=float, default=0.5,
        help="Connection timeout (seconds)"
    )

    # Optional threading argument (disabled by default)
    # parser.add_argument("--threads", type=int, default=1,
    #                     help="Number of threads to use")

    args = parser.parse_args()

    host = args.host
    start_port = args.start
    end_port = args.end
    timeout = args.timeout

    # Scan header
    print(f"[*] Scanning host: {host}")
    print(f"[*] Port range:    {start_port}–{end_port}")
    print(f"[*] Start time:    {datetime.now()}\n")

    # Simple single-threaded scan-
    try:
        for port in range(start_port, end_port + 1):
            if scan_port(host, port, timeout=timeout):
                print(f"[+] Port {port} is open")

    except KeyboardInterrupt:
        print("\n[!] Scan interrupted by user.")

    print("\n[*] Scan complete at", datetime.now())


if __name__ == "__main__":
    main()
