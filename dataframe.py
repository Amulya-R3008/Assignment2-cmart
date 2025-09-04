import pandas as pd

# Create data for 5 students
data = {
    "Name": ["Aarav", "Diya", "Rohan", "Sneha", "Karthik"],
    "Marks": [72, 95, 67, 89, 83]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Student DataFrame:")
print(df)

# Filter students who scored more than 80
high_scorers = df[df["Marks"] > 80]

print("\nStudents who scored more than 80:")
print(high_scorers)
