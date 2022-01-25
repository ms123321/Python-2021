import re
import csv
import pandas as pd


dataframe1 = pd.read_csv("DATAtoCSV.txt")
dataframe1.to_csv('DATAtoCSV.csv', index= None)


#COPY DATA FROM UDP DATASTREAM and put it in a text file called datatest.txt
#run this program and get a csv with all the data 












#with open('datatest.txt') as file:
#    while (line := file.readline().rstrip('')):
#       sline = line.split(',')
#       )
#        print(line)
