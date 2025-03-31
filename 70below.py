import csv
r=0
with open('scores.csv','r') as file:
      csv_reader = csv.reader(file)
      header = next(csv_reader)
      for row in csv_reader:
            row.append(row)
            row[1]=int(row[1])
            if row[1]>=70:
               print(row[0])
            
