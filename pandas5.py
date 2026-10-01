import pandas as pd

data = {
    "Order_ID": [1, 2, 3, 4, 5],
    "Customer": ["Amit", "Rahul", "Sneha", "Priya", "Akash"],
    "Product": ["Laptop", "Mobile", "TV", "Keyboard", "Monitor"],
    "Quantity": [1, 2, 1, 5, 2],
    "Price": [60000, 25000, 45000, 1500, 12000],
    "Discount": [2000, 1000, 3000, 500, 1000]
}

df = pd.DataFrame(data)

df["Final_Amount"] = (df["Quantity"] * df["Price"]) - df["Discount"]

print("All Orders:")
print(df)

print("\nOrders above 5000:")
print(df[df["Final_Amount"] > 5000])

print("\nHighest-value order:")
print(df.loc[df["Final_Amount"].idxmax()])

print("\nAverage order value:")
print(df["Final_Amount"].mean())
