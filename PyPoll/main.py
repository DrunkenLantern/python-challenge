import csv
elect=r'C:\Users\Sebas\Desktop\python-challenge\PyPoll\election_data.csv'

with open(elect, 'r') as elect_data:
    
    elect_csv = csv.reader(elect_data, delimiter=",")
    print(elect_csv)

    Head = next(elect_csv)
    print(f"CSV Header: {Head}")