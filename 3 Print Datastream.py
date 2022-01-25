#with open("datatest.txt", "r") as f:
#    for line in f.read().split("\n")[::]:
 #       print(line)
import itertools
import pandas as pd
import numpy as np
################################################################################################################
### Seperates the datastream so that each stream is printed in order and by the reading type


## NEXT PROGRAM " textTOcsv.py" 
#sqeeze(right click console after hitting f5)
# copy and paste the  the output from each print into file called DATAtoCSV.txt




#takes the rows with eeg data
 
with open("DATA.txt", 'r') as f:
        for line in f.readlines():
         if "eeg" in line:
          print(line)

#takes the rows with accel data

with open("DATA.txt", 'r') as f:
        for line in f.readlines():
         if "accel" in line:
          print(line)


#takes the rows with emg data


with open("DATA.txt", 'r') as f:
        for line in f.readlines():
         if "ecm" in line:
          print(line)

with open("DATA.txt", 'r') as f:
        for line in f.readlines():
         if "Bandpower" in line:
          print(line)




###can squeeze the text and copy and paste into TXT TO CSV program 

