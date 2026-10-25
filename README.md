# Study Tracker

#### Video Demo: (https://www.youtube.com/watch?v=TdO9coFlCaA)

#### Description:

Study Tracker is a command-line program that helps you log how long you study each subject and see where your time is actually going. You add a session by entering a subject and the number of minutes, and the program saves it to a CSV file along with today's date. At any point you can ask for a summary, which totals the minutes per subject and prints a clean table showing minutes and hours.

## How to use

Install the dependencies:

    pip install -r requirements.txt

Run the program:

    python project.py

Then choose one of the options:

- `a` to add a session (enter a subject, then minutes)
- `s` to view the summary table
- `q` to quit

Run the tests:

    pytest test_project.py

## Files

- **project.py**: the main program. It contains `main` and these functions:
  - `validate_minutes(minutes)`: checks that the input is a positive whole number and returns it as an int, otherwise raises a `ValueError`.
  - `add_session(subject, minutes, filename)`: validates the subject and minutes, then appends a row (date, subject, minutes) to the CSV file.
  - `load_sessions(filename)`: reads the CSV and returns a list of sessions. Returns an empty list if the file doesn't exist yet.
  - `summarize(sessions)`: uses a dictionary to add up total minutes per subject.
  - `format_summary(totals)`: builds the summary table using the `tabulate` library.
- **test_project.py**: pytest tests for the functions above. File-based tests use a temporary file so they never touch real data.
- **requirements.txt**: the libraries needed to run the project (`tabulate`, `pytest`).
- **sessions.csv**: created automatically the first time you add a session.

