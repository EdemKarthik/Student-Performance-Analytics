# Student Performance Analytics System
This Python project analyzes student scores from a dataset and produces a
summary of academic performance. It uses pandas to calculate results and
exports the processed student records to a CSV file.

## Features
*Displays the student records, including department, subject scores, and
  attendance.
*Calculates each student's total and average score across HTML, CSS,
  JavaScript, Java, and Python.
*Assigns a letter grade based on the average score:
  -O: above 95
  -A: above 85
  -B: above 70
  -C: above 60
  -D: above 50
  -E: above 45
  -F: 45 or below
*Marks students as Pass when their average score is at least 40; otherwise,
  marks them as Fail.
*Ranks students by total score and reports overall and subject-wise
  performance, as well as the top three performers.
*Saves the records and calculated results to `Students_Output.csv`.

## Input data
The program reads `Students.csv` from the project directory. It expects
student ID, name, department, scores for the five subjects listed above, and
attendance in whitespace-aligned columns, with a header row.

## Requirements
-Python
-pandas
-NumPy

Install the Python packages if needed:
```bash
python -m pip install pandas numpy
```

## Run
From the project directory, run:
```bash
python main.py
```

The analytics are printed in the terminal, and the processed dataset is
written to `Students_Output.csv` in the project directory.
