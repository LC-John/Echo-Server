# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 15:32:15 2018

@author: DrLC
"""

import socket
import threading
import sys
    
DEFAULT_WAITLINE = 100
DEFAULT_PORT = 2333
DEFAULT_TIMEOUT = -1
DEFAULT_BUFSIZE = 1024

def echo_server(client, timeout, bufsize):
    
    try:
        if timeout > 0:
            client.settimeout(timeout)
        print ("Client "+str(client.getpeername())+" connected!")
        buf = client.recv(bufsize)
        str_buf = str(buf, encoding="utf-8")
        print ("From client "+str(client.getpeername())+" > "+str_buf)
        client.send(buf)
        print ("Client "+str(client.getpeername())+" finished!")
    except socket.timeout:
        print ("Client "+str(client.getpeername())+" timeout!")
    except:
        print ("Client "+str(client.getpeername())+" shutdown connection!")
    client.close()
    
def main(args):
    
    waitline = args[0]
    port = args[1]
    timeout = args[2]
    bufsize = args[3]

    print ("Server Config:")
    print ("\tlisten num: "+str(waitline))
    print ("\tlisten port: "+str(port))
    print ("\ttimeout: "+str(timeout))
    print ("\tbuffer size: "+str(bufsize))
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    sock.bind(('localhost', port))  
    sock.listen(waitline)
    
    print ("Server run forever!")
    
    while True:  
        client,address = sock.accept()  
        thread = threading.Thread(target=echo_server,
                                  args=(client, timeout, bufsize))
        thread.start()
    
def print_help():
    
    print ("+---------------------------------+")
    print ("|                                 |")
    print ("|           Echo Server           |")
    print ("|                                 |")
    print ("|           by DRLC (ZHZ)         |")
    print ("|            zhang_hz@pku.edu.cn  |")
    print ("|                                 |")
    print ("+---------------------------------+")
    print ()
    print ()
    print ("This is a simple echo server implementation.")
    print ()
    print ("Use the command to simply run the server:")
    print ("\tpython3 "+str(sys.argv[0]))
    print ()
    print ("Arguments are listed as below:")
    print ("\t--port\tserver listen port\n\tdefault value -- "+str(DEFAULT_PORT))
    print ("\t--listen\tserver listen number\n\tdefault value -- "+str(DEFAULT_WAITLINE))
    print ("\t--timeout\tserver timeout\n\tno timeout when negative\n\tdefault value -- "+str(DEFAULT_TIMEOUT))
    print ("\t--buffer\tserver buffer\n\t\tdefault value "+str(DEFAULT_BUFSIZE))
    
if __name__ == "__main__":
    
    waitline = DEFAULT_WAITLINE
    port = DEFAULT_PORT
    timeout = DEFAULT_TIMEOUT
    bufsize = DEFAULT_BUFSIZE
    
    for arg_idx in range(len(sys.argv)):
        if sys.argv[arg_idx] == "-h" or sys.argv[arg_idx] == "--help":
            print_help()
            exit(0)
        elif sys.argv[arg_idx] == "--port":
            port = int(sys.argv[arg_idx+1])
        elif sys.argv[arg_idx] == "--listen":
            waitline = int(sys.argv[arg_idx+1])
        elif sys.argv[arg_idx] == "--timeout":
            timeout = int(sys.argv[arg_idx+1])
        elif sys.argv[arg_idx] == "--buffer":
            bufsize = int(sys.argv[arg_idx+1])
        
    main([waitline, port, timeout, bufsize])