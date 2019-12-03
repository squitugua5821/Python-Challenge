import pandas as pd

csv_path = "budget_data.csv"

budget_df = pd.read_csv(csv_path, encoding="utf-8")
# print(budget_df.head(10))

total_months = (budget_df["Date"].count())
total_amount = (budget_df["Profit/Losses"].sum())
average_amount = (budget_df["Profit/Losses"].mean())

max_profit = (budget_df["Profit/Losses"].max())
max_date = budget_df.loc[budget_df["Profit/Losses"] == max_profit, "Date"]
max_profit = max_date.iloc[0]

min_profit = (budget_df["Profit/Losses"].min())
min_date = budget_df.loc[budget_df["Profit/Losses"] == min_profit, "Date"]
min_profit = min_date.iloc[0]

print("Total Months: ", total_months)
print("Total: ", total_amount)
print("Average Change: ", average_amount)
print("Greatest Increase in Profits: ", max_date, max_profit)
print("Greatest Decrease in Profits: ", min_date, min_profit)
