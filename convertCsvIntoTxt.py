import csv

output=open('comments-1.txt','w')

with open('comments.csv',"rt") as f:
  for row in f:
    output.write(row.replace(","," "))