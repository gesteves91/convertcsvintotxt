import csv

output=open('comments-3.txt','w')

with open('comments-3.csv',"rt") as f:
  for row in f:
    output.write(row.replace(","," "))