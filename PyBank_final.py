import os
import csv

csvpath=os.path.join("C:/Users/agp07/Instructions/PyBank/Resources/budget_data.csv")
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    print(csvreader)
    csv_header = next(csvreader)
    
    Total_month = []
    revenue = []
    revenue_change = []
    monthly_change = []

    print(f"Header: {csv_header}")
#Total Month
    for row in csvreader:
        Total_month.append(row[0])
        revenue.append(row[1])
    print(len(Total_month))
#revenue
    revenue_int = map(int,revenue)
    total_revenue = (sum(revenue_int))
    print(total_revenue)
#Average change
    i = 0
    for i in range(len(revenue) - 1):
        profit_loss = int(revenue[i+1]) - int(revenue[i])

        revenue_change.append(profit_loss)
    Total = sum(revenue_change)

    monthly_change = Total / len(revenue_change)

print(monthly_change)

#Greatest increase

profit_Inc = max(revenue_change)
print(profit_Inc)
a = revenue_change.index(profit_Inc)
month_increase = Total_month[a+1]

profit_decrease = min(revenue_change)
print(profit_decrease)
b = revenue_change.index(profit_decrease)
month_decrease = Total_month[b+1]

#print all statements

print(f'Financial Analysis')
print(f'-------------------------------------')

print("Total months: " + str(len(Total_month)))
print("Total: $ " + str(total_revenue))
print("Average Change: $" + str(monthly_change))
print(f"Greatest Increase in Profits: {month_increase} (${profit_Inc})")
print(f"Greatest Decrease in Profits: {month_decrease} (${profit_decrease})")





