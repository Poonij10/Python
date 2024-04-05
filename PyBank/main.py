import csv
import pandas as pd

csv_file_path = r"C:\Users\jaspe\OneDrive\Desktop\Classwork\Python\PyBank\Resources\budget_data.csv"
data = pd.read_csv(csv_file_path)


total_months = 0

net_profit_losses = 0

profit_losses_changes = []

previous_profit_loss = None

greatest_increase = ["", 0]

greatest_decrease = ["", 0]



with open(csv_file_path, "r") as file:

    csv_reader = csv.reader(file)

    

    next(csv_reader)

    

    for row in csv_reader:

        total_months += 1

        

        profit_loss = int(row[1])

        

        net_profit_losses += profit_loss

        

        if previous_profit_loss is not None:

            profit_loss_change = profit_loss - previous_profit_loss

            profit_losses_changes.append(profit_loss_change)

            

            if profit_loss_change > greatest_increase[1]:

                greatest_increase = [row[0], profit_loss_change]

            elif profit_loss_change < greatest_decrease[1]:

                greatest_decrease = [row[0], profit_loss_change]



        previous_profit_loss = profit_loss



average_change = sum(profit_losses_changes) / len(profit_losses_changes)



print("Financial Analysis")

print("---------------------------------")

print(f"Total Months: {total_months}")

print(f"Total: ${net_profit_losses}")

print(f"Average Change: ${average_change:.2f}")

print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")

print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

