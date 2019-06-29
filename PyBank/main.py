

import os
import csv

csvpath=os.path.join("budget_data.csv")

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header=next(csvreader)
    
    prev=[]
    diff=[]
    aver=0
    total_change=0
    low_price=0
    great_price=0
    total_row=0
    total_amount=0

    low_month=""
    great_month=""
    

    
    
    for row in csvreader:
        total_row+=1
        total_amount+=int(row[1])
        
        
        if total_row==1:
            diff=row[1]
            prev.append(row[1])
            index=0
            

        else:
            diff=int(row[1])-int(prev[index])
            prev.append(row[1])
            index+=1
            total_change=total_change+diff
          
        
        if int(diff)<low_price:
            
            low_price=int(diff)
            low_month=row[0]
            
        if int(diff)>great_price:
            great_price=int(diff)
            great_month=row[0]
    
    change_num=total_row-1
    aver=round(total_change/change_num,2)
    
    print ("Financial Analysis")
    print ("----------------------------")
    print (f"Total Months:{total_row}")
    print (f"Total:${total_amount}")
    print (f"Average Change: $ {aver}")
    print (f"Greatest Increase in Profits: {great_month}(${great_price})")
    print (f"Greatest Decrease in Profits: {low_month}(${low_price})")

output_path=os.path.join("budget_summary.txt")

with open (output_path, "w",newline="") as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months:{total_row}\n")
    file.write(f"Total:${total_amount}\n")
    file.write(f"Average Change: $ {aver}\n")
    file.write(f"Greatest Increase in Profits: {great_month}(${great_price})\n")
    file.write(f"Greatest Decrease in Profits: {low_month}(${low_price})\n")



