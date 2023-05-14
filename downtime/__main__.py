# Downtime Diary
# A simple and lightweight downtime logger for your linux server
# Github: https://www.github.com/awesomelewis2007/downtime_diary
# Licence: GNU General Public License v3.0
# By: Lewis Evans

import os
import sys

try:
    from colorama import Fore, Back, Style
except ImportError:
    print("Colorama is not installed. Please install it using 'pip install colorama'")
    sys.exit(1)
VERSION = "0.1.0"

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("No parameters given. Type 'downtime help' for help")
    elif sys.argv[1] == "add":
        print("Welcome to downtime diary")
        print(
            "Please enter the date and time the downtime started in the format DD/MM/YYYY HH:MM"
        )
        start = input("Start time: ")
        print(
            "Please enter the date and time the downtime ended in the format DD/MM/YYYY HH:MM"
        )
        end = input("End time: ")
        if "-" in start:
            start = start.replace("-", "")
        if "-" in end:
            end = end.replace("-", "")
        print("Please enter the reason for the downtime")
        reason = input("Reason: ")
        print("Please enter the severity of the downtime")
        while True:
            print("Severity levels:")
            print("\tMinor")
            print("\tMajor")
            print("\tCritical")
            print("\tMaintenance")
            severity = input("Severity: ")
            if (
                severity.lower() == "minor"
                or severity.lower() == "major"
                or severity.lower() == "critical"
                or severity.lower() == "maintenance"
            ):
                break
            else:
                print("Invalid severity. Please enter a valid severity")
        print("Do you want to add a note to the downtime? (y/n)")
        while True:
            note = input("Note: ")
            if note.lower() == "y" or note.lower() == "n":
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'")
        if note.lower() == "y":
            print("Please enter the note")
            note = input("Note: ")
        else:
            note = "None"
        if os.path.exists(os.path.expanduser("~/.downtimes.log")):
            with open(os.path.expanduser("~/.downtimes.log"), "a") as f:
                if severity.lower() == "minor":
                    f.write(
                        "[!] MINOR DOWNTIME-"
                        + start
                        + "-"
                        + end
                        + "-"
                        + reason
                        + "-"
                        + severity
                        + "-"
                        + note
                    )
                elif severity.lower() == "major":
                    f.write(
                        "[x] MAJOR DOWNTIME-"
                        + start
                        + "-"
                        + end
                        + "-"
                        + reason
                        + "-"
                        + severity
                        + "-"
                        + note
                    )
                elif severity.lower() == "critical":
                    f.write(
                        "[X] CRITICAL DOWNTIME-"
                        + start
                        + "-"
                        + end
                        + "-"
                        + reason
                        + "-"
                        + severity
                        + "-"
                        + note
                    )
                elif severity.lower() == "maintenance":
                    f.write(
                        "[*] MAINTENANCE-"
                        + start
                        + "-"
                        + end
                        + "-"
                        + reason
                        + "-"
                        + severity
                        + "-"
                        + note
                    )

        else:
            with open(os.path.expanduser("~/.downtimes.log"), "w") as f:
                if severity.lower() == "minor":
                    f.write(
                        "[!] MINOR DOWNTIME-"
                        + start
                        + "-"
                        + end
                        + "-"
                        + reason
                        + "-"
                        + severity
                        + "-"
                        + note
                    )
                elif severity.lower() == "major":
                    f.write(
                        "[x] MAJOR DOWNTIME-"
                        + start
                        + "-"
                        + end
                        + "-"
                        + reason
                        + "-"
                        + severity
                        + "-"
                        + note
                    )
                elif severity.lower() == "critical":
                    f.write(
                        "[X] CRITICAL DOWNTIME-"
                        + start
                        + "-"
                        + end
                        + "-"
                        + reason
                        + "-"
                        + severity
                        + "-"
                        + note
                    )
                elif severity.lower() == "maintenance":
                    f.write(
                        "[*] MAINTENANCE-"
                        + start
                        + "-"
                        + end
                        + "-"
                        + reason
                        + "-"
                        + severity
                        + "-"
                        + note
                    )

    elif sys.argv[1] == "view":
        if os.path.exists(os.path.expanduser("~/.downtimes.log")):
            with open(os.path.expanduser("~/.downtimes.log"), "r") as f:
                log = f.read()
                start = log.split("-")[1]
                end = log.split("-")[2]
                reason = log.split("-")[3]
                severity = log.split("-")[4]
                note = log.split("-")[5]

                if log.startswith("[!]"):
                    print(Fore.YELLOW + "[!] Minor downtime" + Style.RESET_ALL)
                    print("Start time: " + start)
                    print("End time: " + end)
                    print("Reason: " + reason)
                    print("Severity: " + severity)
                    print("Note: " + note)

                elif log.startswith("[x]"):
                    print(Fore.RED + "[x] Major downtime" + Style.RESET_ALL)
                    print("Start time: " + start)
                    print("End time: " + end)
                    print("Reason: " + reason)
                    print("Severity: " + severity)
                    print("Note: " + note)

                elif log.startswith("[X]"):
                    print(Fore.RED + "[X] Critical downtime" + Style.RESET_ALL)
                    print("Start time: " + start)
                    print("End time: " + end)
                    print("Reason: " + reason)
                    print("Severity: " + severity)
                    print("Note: " + note)

                elif log.startswith("[*]"):
                    print(Fore.BLUE + "[*] Maintenance" + Style.RESET_ALL)
                    print("Start time: " + start)
                    print("End time: " + end)
                    print("Reason: " + reason)
                    print("Severity: " + severity)
                    print("Note: " + note)
        else:
            print("The log file doesn't exist. Please add a downtime entry first")

    elif sys.argv[1] == "clear":
        print("Are you sure you want to clear the log? (y/n)")
        while True:
            sure = input("Sure: ")
            if sure.lower() == "y" or sure.lower() == "n":
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'")
        if sure.lower() == "y":
            if os.path.exists(os.path.expanduser("~/.downtimes.log")):
                with open(os.path.expanduser("~/.downtimes.log"), "w") as f:
                    f.write("")
            else:
                print("The log file doesn't exist. Please add a downtime entry first")
        else:
            print("The log file wasn't cleared")

    elif sys.argv[1] == "help":
        print("Downtime diary help")
        print("downtime add - Add a downtime entry")
        print("downtime view - View the last downtime entry")
        print("downtime clear - Clear the log")
        print("downtime help - View this help page")

    elif sys.argv[1] == "version":
        print("Downtime diary version " + VERSION)

    elif sys.argv[1] == "about":
        print("Downtime diary is a simple command line tool to keep track of downtime")
        print("Downtime diary was created by awesomelewis2007")
        print("Downtime diary is licensed under the GNUv3 license")

    else:
        print("Invalid command. Please enter a valid command")
