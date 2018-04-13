# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 15:34:44 2018

@author: DrLC
"""

import socket
import sys

DEFAULT_IP = 'localhost'
DEFAULT_PORT = 2333
DEFAULT_BUFSIZE = 1024
DEFAULT_TIMEOUT = -1

def print_help():
    
    print ("+---------------------------------+")
    print ("|                                 |")
    print ("|           Echo Client           |")
    print ("|                                 |")
    print ("|           by DRLC (ZHZ)         |")
    print ("|            zhang_hz@pku.edu.cn  |")
    print ("|                                 |")
    print ("+---------------------------------+")
    print ()
    print ()
    print ("This is a simple echo client implementation.")
    print ()
    print ("Use the command to simply run the client:")
    print ("\tpython3 "+str(sys.argv[0]))
    print ()
    print ("Arguments are listed as below:")
    print ("\t--ip\tserver ip\n\tdefault value -- "+str(DEFAULT_IP))
    print ("\t--port\tserver port\n\tdefault value -- "+str(DEFAULT_PORT))
    print ("\t--timeout\tserver timeout\n\tno timeout when negative\n\tdefault value -- "+str(DEFAULT_TIMEOUT))
    print ("\t--buffer\tclient buffer\n\t\tdefault value "+str(DEFAULT_BUFSIZE))

def main(args):

    server_ip = args[0]
    server_port = args[1]
    bufsize = args[3]
    timeout = args[2]
    
    print ("Client Config:")
    print ("\tserver ip: "+str(ip))
    print ("\tserver port: "+str(port))
    print ("\ttimeout: "+str(timeout))
    print ("\tbuffer size: "+str(bufsize))

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
        sock.connect((server_ip, server_port))
    except:
        print ("Some error occurred while connecting to the server...")
        return
        
    print ("Connected to server "+str(sock.getpeername())+".")
    
    try:
        msg = input("To server < ")
        sock.send(bytes(msg, encoding="utf-8"))
        if timeout > 0:
            sock.settimeout(timeout)
        buf = sock.recv(bufsize)
        str_buf = str(buf, encoding="utf-8")
        print ("From server > "+str_buf)
    except socket.timeout:
        print ("Server timeout!")
    except:
        print ("Server shutdown connection!")
        
    addr = sock.getpeername()
    sock.close()
    print ("Disconnected from server "+str(addr)+".")

if __name__ == "__main__":
    
    ip = DEFAULT_IP
    port = DEFAULT_PORT
    timeout = DEFAULT_TIMEOUT
    bufsize = DEFAULT_BUFSIZE
    
    for arg_idx in range(len(sys.argv)):
        if sys.argv[arg_idx] == "-h" or sys.argv[arg_idx] == "--help":
            print_help()
            exit(0)
        elif sys.argv[arg_idx] == "--timeout":
            timeout = int(sys.argv[arg_idx+1])
        elif sys.argv[arg_idx] == "--port":
            port = int(sys.argv[arg_idx+1])
        elif sys.argv[arg_idx] == "--ip":
            ip = str(sys.argv[arg_idx+1])
        elif sys.argv[arg_idx] == "--buffer":
            bufsize = int(sys.argv[arg_idx+1])
    
    main([ip, port, timeout, bufsize])
    
    