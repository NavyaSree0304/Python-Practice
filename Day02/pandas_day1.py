import pandas as pd

students = {
    "Name": ["Navya", "Rahul", "Priya"],
    "Age": [20, 21, 19],
    "Branch": ["AIML", "CSE", "ECE"]
}

df = pd.DataFrame(students)

print(df)

print("\nNames")
print(df["Name"])

print("\nAges")
print(df["Age"])

print("\nFirst Row")
print(df.loc[0])
