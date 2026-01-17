#import the csv module
import csv

#open the csv file
f = open("emp_details.csv", "r")

#read the csv file
rf = csv.reader(f, delimiter=",")

#output the content of the csv file
#This loops through each row and checks if the 4th column (index 3) is "HR"
for row in rf:
    if row[3] == "HR":
        print(row)

#close the csv file
f.close()