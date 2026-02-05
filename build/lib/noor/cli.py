import time
from datetime import datetime
import os
import sys

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    clear_screen()
    print("🌍 Noor — Live Age Calculator")
    print("Enter your Date of Birth (YYYY-MM-DD)")
    dob = input("> ").strip()

    try:
        birth_date = datetime.strptime(dob, "%Y-%m-%d")
    except ValueError:
        print("❌ Invalid date format. Use YYYY-MM-DD")
        sys.exit(1)

    try:
        while True:
            now = datetime.utcnow()
            diff = now - birth_date

            total_seconds = int(diff.total_seconds())
            minutes = total_seconds // 60
            hours = total_seconds // 3600
            days = diff.days
            years = total_seconds / (365.2425 * 24 * 3600)

            clear_screen()
            print("🌍 Noor — Your Life on Earth")
            print("--------------------------------")
            print(f"Years   : {years:.9f}")
            print(f"Days    : {days}")
            print(f"Hours   : {hours}")
            print(f"Minutes : {minutes}")
            print(f"Seconds : {total_seconds}")
            print("--------------------------------")
            print("Press Ctrl + C to exit")

            time.sleep(1)

    except KeyboardInterrupt:
        print("\n👋 Goodbye!")

if __name__ == "__main__":
    main()
