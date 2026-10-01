import pandas as pd

patients = {
    "P001": 45,
    "P002": 65,
    "P003": 72,
    "P004": 35,
    "P005": 80
}

s = pd.Series(patients)

print("Patient Ages:")
print(s)

print("\nAverage Age:", s.mean())
print("Oldest Patient:", s.max())
print("Youngest Patient:", s.min())

print("\nPatients above 60:")
print(s[s > 60])
