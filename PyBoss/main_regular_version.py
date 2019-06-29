
import os 
import re
import csv
import datetime

csvpath = os.path.join("employee_data.csv")


first=[]
last=[]
DOB=[]
SSN=[]
State=[]
ids=[]

output="employee_data_reformatted.csv"

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}



with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
 
    csv_header = next(csvreader)

    for row in csvreader:
        ids.append(row[0])
        first.append(row[1].split(" ")[0])
        last.append(row[1].split(" ")[1])
        #row[3]=re.sub(r"\d{3}-\d{2}","***-**",row[3])
        SSN.append(re.sub(r"\d{3}-\d{2}","***-**",row[3]))
        #row[4]=us_state_abbrev[row[4]]
        State.append(us_state_abbrev[row[4]])
        #row[2]=datetime.datetime.strptime(row[2], '%Y-%m-%d').strftime('%m/%d/%y')
        DOB.append(datetime.datetime.strptime(row[2], '%Y-%m-%d').strftime('%m/%d/%y'))


with open(output,"w",newline="") as df:
    writer=csv.writer(df)
    result=zip(ids,first,last,DOB,SSN,State)
    writer.writerow(["Emp ID", "First Name","Last Name","DOB","SSN","State"])
    writer.writerows(result)
        