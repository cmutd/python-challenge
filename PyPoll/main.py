
import os
import csv



csvpath = os.path.join("election_data.csv")
total=0
count=0
highest=0
per=0
candidates={}
winner=""

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)


    for row in csvreader:
        total+=1
        candidates[row[2]]=candidates.get(row[2],0)+1

    
    print ("Election Results")
    print ("-------------------------")
    print (f"Total Votes: {total}")
    print ("-------------------------")
    
    for candidate in candidates.keys():

        per="{0:.3f}".format(candidates[candidate]/total*100,3)
        if candidates[candidate]>highest:
            highest=candidates[candidate]
            winner=candidate
        print (f"{candidate}: {per}% ({candidates[candidate]})")
        
    print ("-------------------------")
    print (f"Winner: {winner}")
    print ("-------------------------")

        
    

    
output_path=os.path.join("election_summary.txt")

with open (output_path, "w",newline="") as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total}\n")
    file.write("-------------------------\n")
    
    for candidate in candidates.keys():

        per="{0:.3f}".format(candidates[candidate]/total*100,3)
        if candidates[candidate]>highest:
            highest=candidates[candidate]
            winner=candidate
        file.write (f"{candidate}: {per}% ({candidates[candidate]})\n")
        
    file.write ("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write ("-------------------------\n")

        
    

    
    