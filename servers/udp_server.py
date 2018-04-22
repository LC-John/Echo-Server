# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 15:10:13 2018

@author: DrLC
"""

import socket 
  
HOST = 'localhost'    
PORT = 2335  
  
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
s.bind((HOST,PORT))
while True:  
    data, addr = s.recvfrom(1024)  
    print ("From client "+str(addr)+" > "+str(data, encoding="utf-8"))
    s.sendto(data, addr)  
s.close()  