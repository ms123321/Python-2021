import socket
import traceback
import csv
import subprocess
import pandas as pd
import numpy as np
import os

######## s

import time
from datetime import datetime



if __name__ == "__main" :
 host ="127.0.0.1"
 port = 12345, 12346 ,12347
 addr = (host, port)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("localhost", 12346)) #more ports need to add more code though for  them 



sock_two = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_two.bind(("localhost", 12345))


sock_three = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_three.bind(("localhost", 12347))

while True:
  data, addr = sock.recvfrom(1024)
  data2, addr = sock_two.recvfrom(1024)
  data3, addr = sock_three.recvfrom(1024)# buffer size is 1024 bytes
  #print("received message: %s" % data) old way of doing data show
 # print("%s" % data , current_time) bugged 
  #print(data)# simpliest way 
  now=datetime.now()
  print(time.time(), datetime.now() ,data )
  print(time.time(), datetime.now() ,data2 )
  print(time.time(), datetime.now() ,data3 )
  
  #df = pd.DataFrame([data[:]])
 # print(df)
  #df.to_csv('Output.csv', index = False)

a = list(data)
s.close()
