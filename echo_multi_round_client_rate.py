# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 19:24:33 2018

@author: DrLC
"""

import socket
import sys
import random
import time

DEFAULT_IP = 'localhost'
DEFAULT_PORT = 2333
DEFAULT_BUFSIZE = 1024
DEFAULT_TIMEOUT = 10
DEFAULT_LENGTH = 1000

def print_help():
    
    print ("+---------------------------------+")
    print ("|                                 |")
    print ("|          Echo Rate Test         |")
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

    global sock
    
    server_ip = args[0]
    server_port = args[1]
    bufsize = args[3]
    timeout = args[2]
    length = args[4]
    
    print ("Rate Testing Client Config:")
    print ("\tserver ip: "+str(ip))
    print ("\tserver port: "+str(port))
    print ("\ttimeout: "+str(timeout))
    print ("\tbuffer size: "+str(bufsize))
    print ("\tlength: "+str(length))

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
        sock.connect((server_ip, server_port))
    except:
        print ("Some error occurred while connecting to the server...")
        return
        
    print ("Connected to server "+str(sock.getpeername())+".")
    goon = True
    slot_size = [0]
    slot_time = [time.time()]
    size = 0
    counter = 0
    while goon:
        try:
            counter += 1
            msg = "0" * length
            sock.send(bytes(msg, encoding="utf-8"))
            if msg == "exit":
                goon = False
                return
            if timeout > 0:
                sock.settimeout(timeout)
            buf = sock.recv(bufsize)
            str_buf = str(buf, encoding="utf-8")
            tmp_size = sys.getsizeof(str_buf)
            slot_time.append(time.time())
            size += tmp_size
            slot_size.append(tmp_size)
            if len(slot_size) >= 100:
                size -= slot_size[0]
                slot_size = slot_size[1:]
                slot_time = slot_time[1:]
            if counter >= 5000:
                counter = 0
                print (("\rEcho rate: %.1f Mbps, %.1f Gbps "
                        % (size / 1000 / (slot_time[-1] - slot_time[0]),
                           size / 1000000 / (slot_time[-1] - slot_time[0]))),
                       end="")
        except socket.timeout:
            print ("Server timeout!")
            goon = False
            return
        except:
            print ("Shutdown!")
            goon = False
            return
        
    addr = sock.getpeername()
    sock.close()
    print ("Disconnected from server "+str(addr)+".")

if __name__ == "__main__":

    ip = DEFAULT_IP
    port = DEFAULT_PORT
    timeout = DEFAULT_TIMEOUT
    bufsize = DEFAULT_BUFSIZE
    length = DEFAULT_LENGTH
    
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
        elif sys.argv[arg_idx] == "--length":
            length = int(sys.argv[arg_idx+1])
    
    main([ip, port, timeout, bufsize, length])
    