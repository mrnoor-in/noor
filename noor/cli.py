import time
from datetime import datetime
import os
import sys

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    clear()
    print("🌍 Noor — Live Age Calculator")
    print("Enter your Date of Birth (YYYY-MM-DD)")
    dob = input("> ").strip()

    try:
        birth = datetime.strptime(dob, "%Y-%m-%d")
    except ValueError:
        print("❌ Invalid date format")
        sys.exit(1)

    try:
        while True:
            now = datetime.utcnow()
            diff = now - birth

            seconds = int(diff.total_seconds())
            minutes = seconds // 60
            hours = seconds // 3600
            days = diff.days
            years = seconds / (365.2425 * 24 * 3600)

            clear()
            print("🌍 Noor — Your Life on Earth")
            print("----------------------------")
            print(f"Years   : {years:.9f}")
            print(f"Days    : {days}")
            print(f"Hours   : {hours}")
            print(f"Minutes : {minutes}")
            print(f"Seconds : {seconds}")
            print("----------------------------")
            print("Press Ctrl+C to exit")

            time.sleep(1)

    except KeyboardInterrupt:
        print("\n👋 Goodbye")

if __name__ == "__main__":
    main()
