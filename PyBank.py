# dependancies
import csv
import os

# files to import
file_to_load = os.path.join('/Resources/Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv')
file_to_output = os.path.join('/analysis/budget_analysis.txt')

# financial parameters
total_months = 0
month_of_change = []
net_month_list = []
greatest_increase = ['', 0]
greatest_decrease = ['', 99999999999999]
total_net = 0

# read csv and convert to list of dictionaries
with open(file_to_load) as finacial_data:
    reader = csv.reader(finacial_data)

    # read header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
first_row = next(reader)
total_months += 1
total_net += int(first_row[1])
prev_net = int(first_row[1])

for row in reader:
# track the total
    total_months += 1
    total_net += int(row[1])

# track the net change
    net_change = int(row[1]) - prev_net
    prev_net = int(row[1])
    net_change_list += [net_chnage]
    month_of_change += [row[0]]
# Calc the greatest increase
    if net_change > greatest_increase[1]:
        greatest_increase[0] = row[0]
        greatest_increase[1] = net_change
# Calc the greatest decrease
    if net_change < greatest_decrease[1]:
        greatest_decrease[0] = row[0]
        greatest_decrease[1] = net_change
# calc the average net change
    net_month_ave = sum(net_change_list / len(net_change_list)
# Output Summary
output = ( 
    f'Financial Analysis\n'
    f'---------------------------\n'
    f'total months: {total_months}\n'
    f'total: ${total_net}\n'
    f'average change: ${net_month_ave:.2f}\n'
    f'greatest increase in profits: {greatest_increase[0]} (${greatest_increase[1]}\n'
    f'greatest decrease in profits: {greatest_decrease[0]} (${greatest_decrease[1]}\n')

# print output
print (output)

# export the results to text file
with open(file_to_output, 'w') as txt_file
    txt_file.write(output)
