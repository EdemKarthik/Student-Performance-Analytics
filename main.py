import pandas as pd 
import numpy as np
df = pd.read_fwf(
    "students.csv",
    skiprows=1,
    header=None,
    names=[
        "Student_ID",
        "Name",
        "Department",
        "Html",
        "CSS",
        "JavaScript",
        "Java",
        "Python",
        "Attendance",
    ],
)
subjects=[
    "Html",
    "CSS",
    "JavaScript",
    "Java",
    "Python"
]
print("\n===STUDENTS DATA===")
print(df.to_string(index=False))

print("\n===TOTAL SCORE===")
df['Total Score'] = df[subjects].sum(axis=1)
print(df.to_string(index=False))

print("\n===AVERAGE SCORE===")
df['Average Score'] = df[subjects].mean(axis=1)
print(df.to_string(index=False))

def grade(x):
    if x > 95:
        return 'O'
    elif x > 85:
        return 'A'
    elif x > 70:
        return 'B'
    elif x > 60:
        return 'C'
    elif x > 50:
        return 'D'
    elif x > 45:
        return 'E'
    else:
        return 'F'
print("\n===GRADES===")
df["Grades"] = df["Average Score"].apply(grade)
print(df.to_string(index=False))

def pass_fail(x):
    return "Pass" if x >= 40 else "Fail"
print("\n===PASS/FAIL===")
df["Pass/Fail"] = df["Average Score"].apply(pass_fail)
print(df.to_string(index=False))

def rank(x):
    df['Rank'] = df['Total Score'].rank(ascending=False, method='min').astype(int)
    return df.sort_values(by='Rank')
print("\n===RANKED STUDENTS===")
ranked_df = rank(df)
print(ranked_df.to_string(index=False))

def performance(x):
    highest_student = df.loc[df['Total Score'].idxmax()]
    lowest_student = df.loc[df['Total Score'].idxmin()]
    performance = {
        'Total Students': len(df),
        'Passed Students': len(df[df['Pass/Fail'] == 'Pass']),
        'Failed Students': len(df[df['Pass/Fail'] == 'Fail']),
        'Highest Performance': highest_student['Total Score'],
        'Lowest Performance': lowest_student['Total Score'],
        'Average Performance': df['Average Score'].mean()
    }
    return performance
print("\n===PERFORMANCE===")
performance = performance(df)
for key, value in performance.items():
    print(f"{key}: {value}")

def Subject_Wise_Performance(x, subjects):
    subject_Wise_performance = {}
    for subject in subjects:
        subject_Wise_performance[subject] = {
            'Highest Score': df[subject].max(),
            'Lowest Score': df[subject].min(),
            'Average Score': df[subject].mean()
        }
    return subject_Wise_performance
print("\n===SUBJECT WISE PERFORMANCE===")
subject_performance = Subject_Wise_Performance(df, subjects)
for subject, performance in subject_performance.items():
    print(f"\n{subject}:")
    for key, value in performance.items():
        print(f"  {key}: {value}")

def Top_Performers(x, n=3):
    top_performers = df.nlargest(n, 'Total Score')
    return top_performers
print("\n===TOP PERFORMERS===")
top_performers = Top_Performers(df[['Student_ID', 'Name', 'Department', 'Total Score', 'Rank']])
print(top_performers.to_string(index=False))

df.to_csv("Students_Output.csv", index=False)