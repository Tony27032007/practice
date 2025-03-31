import csv
r=0
with open('scores.csv','r') as file:
      csv_reader = csv.reader(file)
      header = next(csv_reader)
      for row in csv_reader:
            row.append(row)
            row[2]=int(row[2])
            if row[2]>=70:
               print(row)
            
