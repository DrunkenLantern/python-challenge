import csv
file=r'C:\Users\Sebas\Desktop\python-challenge\PyBank\budget_data.csv'

with open(file, 'r') as bud_cs:
    
    the_csv = csv.reader(bud_cs, delimiter=",")
    print(the_csv)

    csv_head = next(the_csv)
    # print(f"CSV Header: {csv_head}")
    counting_row = sum(1 for row in the_csv)
    print(counting_row if counting_row else 'Empty')
 
    


        
    