import os
import csv
import numpy as np
import pandas as pd


FILE_NAME = "farm_records.csv"

HEADERS = [
    "CropID",
    "Crop",
    "Season",
    "Area",
    "Production",
    "SellingPrice",
    "Seeds",
    "Fertilizer",
    "Pesticides",
    "Labor",
    "Irrigation",
    "Machinery",
    "Transportation",
    "Other",
    "TotalCost",
    "Revenue",
    "Profit",
    "ProfitPercentage",
    "CostPerQuintal"
]


# --------------------------------------------------
# CREATE CSV FILE
# --------------------------------------------------

def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(HEADERS)


# --------------------------------------------------
# INPUT VALIDATION
# --------------------------------------------------

def get_float(message):
    while True:
        try:
            value = float(input(message))

            if value < 0:
                print("Please enter a positive value.")
            else:
                return value

        except ValueError:
            print("Invalid input! Please enter a number.")


def get_int(message):
    while True:
        try:
            value = int(input(message))

            if value < 0:
                print("Please enter a positive value.")
            else:
                return value

        except ValueError:
            print("Invalid input! Please enter a number.")


# --------------------------------------------------
# ADD CROP
# --------------------------------------------------

def add_crop():

    print("\n========== ADD CROP RECORD ==========")

    crop_id = input("Enter Crop ID: ").strip()

    crop_name = input("Enter Crop Name: ").strip()
    season = input("Enter Season (Kharif/Rabi/Summer): ").strip()

    area = get_float("Enter Land Area (Acres): ")
    production = get_float("Enter Production (Quintal): ")
    selling_price = get_float("Enter Selling Price per Quintal: ")

    print("\n----- ENTER EXPENSES -----")

    seeds = get_float("Seeds: ")
    fertilizer = get_float("Fertilizer: ")
    pesticides = get_float("Pesticides: ")
    labor = get_float("Labor: ")
    irrigation = get_float("Irrigation: ")
    machinery = get_float("Machinery: ")
    transportation = get_float("Transportation: ")
    other = get_float("Other Expenses: ")

    # Total cost
    total_cost = (
        seeds
        + fertilizer
        + pesticides
        + labor
        + irrigation
        + machinery
        + transportation
        + other
    )

    # Revenue
    revenue = production * selling_price

    # Profit
    profit = revenue - total_cost

    # Profit percentage
    if total_cost > 0:
        profit_percentage = (profit / total_cost) * 100
    else:
        profit_percentage = 0

    # Cost per quintal
    if production > 0:
        cost_per_quintal = total_cost / production
    else:
        cost_per_quintal = 0

    record = [
        crop_id,
        crop_name,
        season,
        area,
        production,
        selling_price,
        seeds,
        fertilizer,
        pesticides,
        labor,
        irrigation,
        machinery,
        transportation,
        other,
        total_cost,
        revenue,
        profit,
        profit_percentage,
        cost_per_quintal
    ]

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(record)

    print("\n====================================")
    print("      CROP RECORD SAVED")
    print("====================================")

    print(f"Total Cost       : ₹{total_cost:.2f}")
    print(f"Revenue          : ₹{revenue:.2f}")

    if profit >= 0:
        print(f"Profit           : ₹{profit:.2f}")
    else:
        print(f"Loss             : ₹{abs(profit):.2f}")

    print(f"Profit Percentage: {profit_percentage:.2f}%")
    print(f"Cost per Quintal : ₹{cost_per_quintal:.2f}")


# --------------------------------------------------
# VIEW ALL RECORDS
# --------------------------------------------------

def view_crops():

    print("\n========== ALL CROP RECORDS ==========")

    try:
        df = pd.read_csv(FILE_NAME)

        if df.empty:
            print("No crop records found.")
            return

        display_columns = [
            "CropID",
            "Crop",
            "Season",
            "Area",
            "Production",
            "TotalCost",
            "Revenue",
            "Profit"
        ]

        print(df[display_columns].to_string(index=False))

    except Exception as e:
        print("Error:", e)


# --------------------------------------------------
# SEARCH CROP
# --------------------------------------------------

def search_crop():

    print("\n========== SEARCH CROP ==========")

    search = input("Enter Crop Name or Crop ID: ").strip()

    try:
        df = pd.read_csv(FILE_NAME)

        result = df[
            (df["CropID"].astype(str).str.lower() == search.lower())
            |
            (df["Crop"].astype(str).str.lower() == search.lower())
        ]

        if result.empty:
            print("Crop not found.")
        else:
            print("\nCrop Found:\n")
            print(result.to_string(index=False))

    except Exception as e:
        print("Error:", e)


# --------------------------------------------------
# DELETE CROP
# --------------------------------------------------

def delete_crop():

    print("\n========== DELETE CROP ==========")

    crop_id = input("Enter Crop ID to delete: ").strip()

    try:
        df = pd.read_csv(FILE_NAME)

        if crop_id not in df["CropID"].astype(str).values:
            print("Crop ID not found.")
            return

        df = df[df["CropID"].astype(str) != crop_id]

        df.to_csv(FILE_NAME, index=False)

        print("Crop record deleted successfully.")

    except Exception as e:
        print("Error:", e)


# --------------------------------------------------
# UPDATE CROP
# --------------------------------------------------

def update_crop():

    print("\n========== UPDATE CROP ==========")

    crop_id = input("Enter Crop ID to update: ").strip()

    try:
        df = pd.read_csv(FILE_NAME)

        index = df.index[df["CropID"].astype(str) == crop_id].tolist()

        if not index:
            print("Crop ID not found.")
            return

        i = index[0]

        print("\nEnter new details.")

        crop_name = input("Crop Name: ").strip()
        season = input("Season: ").strip()

        area = get_float("Land Area: ")
        production = get_float("Production: ")
        selling_price = get_float("Selling Price: ")

        print("\n----- Expenses -----")

        seeds = get_float("Seeds: ")
        fertilizer = get_float("Fertilizer: ")
        pesticides = get_float("Pesticides: ")
        labor = get_float("Labor: ")
        irrigation = get_float("Irrigation: ")
        machinery = get_float("Machinery: ")
        transportation = get_float("Transportation: ")
        other = get_float("Other: ")

        total_cost = (
            seeds
            + fertilizer
            + pesticides
            + labor
            + irrigation
            + machinery
            + transportation
            + other
        )

        revenue = production * selling_price
        profit = revenue - total_cost

        if total_cost > 0:
            profit_percentage = (profit / total_cost) * 100
        else:
            profit_percentage = 0

        if production > 0:
            cost_per_quintal = total_cost / production
        else:
            cost_per_quintal = 0

        df.loc[i, "Crop"] = crop_name
        df.loc[i, "Season"] = season
        df.loc[i, "Area"] = area
        df.loc[i, "Production"] = production
        df.loc[i, "SellingPrice"] = selling_price
        df.loc[i, "Seeds"] = seeds
        df.loc[i, "Fertilizer"] = fertilizer
        df.loc[i, "Pesticides"] = pesticides
        df.loc[i, "Labor"] = labor
        df.loc[i, "Irrigation"] = irrigation
        df.loc[i, "Machinery"] = machinery
        df.loc[i, "Transportation"] = transportation
        df.loc[i, "Other"] = other
        df.loc[i, "TotalCost"] = total_cost
        df.loc[i, "Revenue"] = revenue
        df.loc[i, "Profit"] = profit
        df.loc[i, "ProfitPercentage"] = profit_percentage
        df.loc[i, "CostPerQuintal"] = cost_per_quintal

        df.to_csv(FILE_NAME, index=False)

        print("Crop record updated successfully.")

    except Exception as e:
        print("Error:", e)


# --------------------------------------------------
# PROFIT ANALYSIS
# --------------------------------------------------

def profit_analysis():

    print("\n========== PROFIT ANALYSIS ==========")

    try:
        df = pd.read_csv(FILE_NAME)

        if df.empty:
            print("No records available.")
            return

        for _, row in df.iterrows():

            print("\n--------------------------------")
            print("Crop:", row["Crop"])

            print(f"Total Cost: ₹{row['TotalCost']:.2f}")
            print(f"Revenue: ₹{row['Revenue']:.2f}")

            if row["Profit"] >= 0:
                print(f"Profit: ₹{row['Profit']:.2f}")
            else:
                print(f"Loss: ₹{abs(row['Profit']):.2f}")

            print(f"Profit %: {row['ProfitPercentage']:.2f}%")
            print(f"Cost/Quintal: ₹{row['CostPerQuintal']:.2f}")

    except Exception as e:
        print("Error:", e)


# --------------------------------------------------
# EXPENSE ANALYSIS
# --------------------------------------------------

def expense_analysis():

    print("\n========== EXPENSE ANALYSIS ==========")

    try:
        df = pd.read_csv(FILE_NAME)

        if df.empty:
            print("No records available.")
            return

        expense_columns = [
            "Seeds",
            "Fertilizer",
            "Pesticides",
            "Labor",
            "Irrigation",
            "Machinery",
            "Transportation",
            "Other"
        ]

        totals = df[expense_columns].sum()

        print("\nTotal Expense by Category:")

        for expense, amount in totals.items():
            print(f"{expense:<20} ₹{amount:.2f}")

        highest_expense = totals.idxmax()

        print("\nHighest Expense Category:")
        print(highest_expense)
        print(f"Amount: ₹{totals.max():.2f}")

    except Exception as e:
        print("Error:", e)


# --------------------------------------------------
# CROP COMPARISON
# --------------------------------------------------

def crop_comparison():

    print("\n========== CROP COMPARISON ==========")

    try:
        df = pd.read_csv(FILE_NAME)

        if df.empty:
            print("No records available.")
            return

        result = df.sort_values(by="Profit", ascending=False)

        columns = [
            "Crop",
            "Season",
            "Production",
            "TotalCost",
            "Revenue",
            "Profit"
        ]

        print(result[columns].to_string(index=False))

        best_crop = result.iloc[0]

        print("\n--------------------------------")
        print("MOST PROFITABLE CROP")
        print("--------------------------------")
        print("Crop:", best_crop["Crop"])
        print(f"Profit: ₹{best_crop['Profit']:.2f}")

    except Exception as e:
        print("Error:", e)


# --------------------------------------------------
# NUMPY ANALYSIS
# --------------------------------------------------

def numpy_analysis():

    print("\n========== NUMPY ANALYSIS ==========")

    try:
        df = pd.read_csv(FILE_NAME)

        if df.empty:
            print("No records available.")
            return

        profits = np.array(df["Profit"].values)
        costs = np.array(df["TotalCost"].values)
        production = np.array(df["Production"].values)

        print("\nProfit Statistics")

        print(f"Total Profit   : ₹{np.sum(profits):.2f}")
        print(f"Average Profit : ₹{np.mean(profits):.2f}")
        print(f"Maximum Profit : ₹{np.max(profits):.2f}")
        print(f"Minimum Profit : ₹{np.min(profits):.2f}")
        print(f"Profit Std Dev : ₹{np.std(profits):.2f}")

        print("\nCost Statistics")

        print(f"Total Cost     : ₹{np.sum(costs):.2f}")
        print(f"Average Cost   : ₹{np.mean(costs):.2f}")

        print("\nProduction Statistics")

        print(f"Total Production   : {np.sum(production):.2f} Quintal")
        print(f"Average Production : {np.mean(production):.2f} Quintal")

    except Exception as e:
        print("Error:", e)


# --------------------------------------------------
# PANDAS ANALYSIS
# --------------------------------------------------

def pandas_analysis():

    print("\n========== PANDAS DATA ANALYSIS ==========")

    try:
        df = pd.read_csv(FILE_NAME)

        if df.empty:
            print("No records available.")
            return

        print("\n----- Dataset -----")
        print(df.to_string(index=False))

        print("\n----- Basic Information -----")
        print("Number of Records:", len(df))

        print("\n----- Average Values -----")
        print("Average Cost:", df["TotalCost"].mean())
        print("Average Revenue:", df["Revenue"].mean())
        print("Average Profit:", df["Profit"].mean())

        print("\n----- Highest Profit -----")

        highest = df.loc[df["Profit"].idxmax()]

        print("Crop:", highest["Crop"])
        print("Profit:", highest["Profit"])

        print("\n----- Lowest Profit -----")

        lowest = df.loc[df["Profit"].idxmin()]

        print("Crop:", lowest["Crop"])
        print("Profit:", lowest["Profit"])

        print("\n----- Season-wise Analysis -----")

        season_analysis = df.groupby("Season")["Profit"].sum()

        print(season_analysis)

    except Exception as e:
        print("Error:", e)


# --------------------------------------------------
# FARM REPORT
# --------------------------------------------------

def farm_report():

    print("\n")
    print("=" * 50)
    print("             FARMSENSE REPORT")
    print("=" * 50)

    try:
        df = pd.read_csv(FILE_NAME)

        if df.empty:
            print("No records available.")
            return

        total_crops = len(df)
        total_area = df["Area"].sum()
        total_production = df["Production"].sum()
        total_cost = df["TotalCost"].sum()
        total_revenue = df["Revenue"].sum()
        total_profit = df["Profit"].sum()

        print(f"Total Crop Records : {total_crops}")
        print(f"Total Land Area    : {total_area:.2f} Acres")
        print(f"Total Production   : {total_production:.2f} Quintal")
        print(f"Total Cost         : ₹{total_cost:.2f}")
        print(f"Total Revenue      : ₹{total_revenue:.2f}")

        if total_profit >= 0:
            print(f"Total Profit       : ₹{total_profit:.2f}")
        else:
            print(f"Total Loss         : ₹{abs(total_profit):.2f}")

        if total_cost > 0:
            overall_percentage = (total_profit / total_cost) * 100
        else:
            overall_percentage = 0

        print(f"Overall Profit %   : {overall_percentage:.2f}%")

        best = df.loc[df["Profit"].idxmax()]

        print("\nMost Profitable Crop")
        print(f"Crop   : {best['Crop']}")
        print(f"Profit : ₹{best['Profit']:.2f}")

        print("=" * 50)

    except Exception as e:
        print("Error:", e)


# --------------------------------------------------
# MAIN MENU
# --------------------------------------------------

def main_menu():

    create_file()

    while True:

        print("\n")
        print("=" * 50)
        print("        🌾 FARMSENSE 🌾")
        print("  Crop Cost & Profit Analyzer")
        print("=" * 50)

        print("1. Add Crop Record")
        print("2. View All Crop Records")
        print("3. Search Crop")
        print("4. Update Crop Record")
        print("5. Delete Crop Record")
        print("6. Profit Analysis")
        print("7. Expense Analysis")
        print("8. Crop Comparison")
        print("9. NumPy Analysis")
        print("10. Pandas Data Analysis")
        print("11. Generate Farm Report")
        print("12. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_crop()

        elif choice == "2":
            view_crops()

        elif choice == "3":
            search_crop()

        elif choice == "4":
            update_crop()

        elif choice == "5":
            delete_crop()

        elif choice == "6":
            profit_analysis()

        elif choice == "7":
            expense_analysis()

        elif choice == "8":
            crop_comparison()

        elif choice == "9":
            numpy_analysis()

        elif choice == "10":
            pandas_analysis()

        elif choice == "11":
            farm_report()

        elif choice == "12":
            print("\nThank you for using FarmSense!")
            print("🌾 Happy Farming! 🌾")
            break

        else:
            print("Invalid choice! Please enter 1-12.")


# --------------------------------------------------
# PROGRAM START
# --------------------------------------------------

if __name__ == "__main__":
    main_menu()