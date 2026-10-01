import pandas as pd

data = {
    "Patient_ID": [1, 2, 3, 4, 5],
    "Name": ["Amit", "Ravi", "Sneha", "Priya", "Raj"],
    "Age": [65, 45, 72, 30, 68],
    "Disease": ["Diabetes", "Fever", "Heart", "Cold", "Diabetes"],
    "Medical_Charges": [60000, 20000, 80000, 10000, 55000]
}

df = pd.DataFrame(data)

print("Patients above 60:")
print(df[df["Age"] > 60])

print("\nAverage medical charge:")
print(df["Medical_Charges"].mean())

print("\nMaximum medical charge:")
print(df["Medical_Charges"].max())

print("\nPatients with charges greater than 50000:")
print(df[df["Medical_Charges"] > 50000])
