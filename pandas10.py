import pandas as pd

products = {
    "Laptop": 50000,
    "Mobile": 25000,
    "Keyboard": 1500,
    "Monitor": 12000,
    "Mouse": 800
}

s = pd.Series(products)

print("Products and Prices:")
print(s)

s = s * 1.10

print("\nPrices after 10% increase:")
print(s)

print("\nMost expensive product:")
print(s.idxmax(), s.max())

print("\nProducts costing more than 1000:")
print(s[s > 1000])
