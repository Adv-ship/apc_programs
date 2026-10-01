import pandas as pd

data = {
    "Product_ID": [1, 2, 3, 4, 5],
    "Product_Name": ["Laptop", "Mobile", "TV", "Keyboard", "Monitor"],
    "Category": ["Electronics", "Electronics", "Electronics", "Accessories", "Electronics"],
    "Price": [50000, 25000, 40000, 1200, 15000],
    "Quantity": [2, 3, 1, 10, 2]
}

df = pd.DataFrame(data)

df["Total_Sales"] = df["Price"] * df["Quantity"]

print("DataFrame:")
print(df)

print("\nTotal Sales:", df["Total_Sales"].sum())

print("\nProducts with sales greater than 10000:")
print(df[df["Total_Sales"] > 10000])

print("\nProduct with maximum sales:")
print(df.loc[df["Total_Sales"].idxmax()])

print("\nAverage Sales:", df["Total_Sales"].mean())
