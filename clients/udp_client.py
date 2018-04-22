# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 15:10:43 2018

@author: DrLC
"""

import socket
  
HOST = '10.1.3.190'  
PORT = 2335
  
def main():

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
    s.connect((HOST,PORT))
    while True:  
        try:
            msg = input("To Server < ")
            s.sendall(bytes(msg, encoding="utf-8"))
            data = s.recv(1024)
            print ("From server > "+str(data, encoding="utf-8"))
        except Exception as e:
            print (e)
            s.close()
            break
    s.close()  
    
if __name__ == "__main__":
    
    main()