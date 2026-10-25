import csv
import sys
from datetime import date
from tabulate import tabulate

FILE = "sessions.csv"


def main():
    print("Study Tracker")
    while True:
        choice = input("(a)dd session, (s)ummary, (q)uit: ").strip().lower()
        if choice == "a":
            subject = input("Subject: ").strip()
            minutes = input("Minutes: ").strip()
            try:
                add_session(subject, minutes)
                print("Saved.")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "s":
            sessions = load_sessions()
            if not sessions:
                print("No sessions yet.")
            else:
                print(format_summary(summarize(sessions)))
        elif choice == "q":
            sys.exit("Bye!")


def validate_minutes(minutes):
    """Return minutes as a positive int, or raise ValueError."""
    try:
        m = int(minutes)
    except (ValueError, TypeError):
        raise ValueError("Minutes must be a whole number")
    if m <= 0:
        raise ValueError("Minutes must be positive")
    return m


def add_session(subject, minutes, filename=FILE):
    """Validate and append a session to the CSV."""
    if not subject:
        raise ValueError("Subject cannot be empty")
    m = validate_minutes(minutes)
    with open(filename, "a", newline="") as f:
        csv.writer(f).writerow([date.today().isoformat(), subject.title(), m])


def load_sessions(filename=FILE):
    """Return a list of (date, subject, minutes) tuples; empty if no file."""
    try:
        with open(filename) as f:
            return [(d, s, int(m)) for d, s, m in csv.reader(f)]
    except FileNotFoundError:
        return []


def summarize(sessions):
    """Return {subject: total_minutes}."""
    totals = {}
    for _, subject, minutes in sessions:
        totals[subject] = totals.get(subject, 0) + minutes
    return totals


def format_summary(totals):
    """Return a grid table string of subject, minutes, hours."""
    rows = [
        [subject, minutes, f"{minutes / 60:.1f}"]
        for subject, minutes in sorted(totals.items())
    ]
    return tabulate(rows, headers=["Subject", "Minutes", "Hours"], tablefmt="grid")


if __name__ == "__main__":
    main()
