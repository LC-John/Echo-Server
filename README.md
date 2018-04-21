# Dummy Chat

This repo is about a set of dummy client-server chat programs.

They are boring. They are useless. They are just for homework.

## Echo

### Echo Server

There are two servers in the directory `servers`. `simple_server.py` is a simple echo server which send back whatever it receives, and then close the socket connection. `server.py` will not close the connection until the client close it.

Both servers have timeout, whose default value is 10 seconds.

You can use the command `python3 server.py` to run the server. If you want to set your own parameters, use the following command to get the help information. 

```
$> python server.py -h
+---------------------------------+
|                                 |
|           Echo Server           |
|                                 |
|           by DRLC (ZHZ)         |
|            zhang_hz@pku.edu.cn  |
|                                 |
+---------------------------------+


This is a simple echo server implementation.

Use the command to simply run the server:
        python3 server.py

Arguments are listed as below:
        --port  server listen port
        default value -- 2333
        --listen        server listen number
        default value -- 100
        --timeout       server timeout
        no timeout when negative
        default value -- 30
        --buffer        server buffer
                default value 1024
```

If you do not want run your own server, I deployed on them on my own server. You may use the client program to connect to my server. The host IP addresses and the ports are shown in the table below.

| Server           | Host IP       | Port |
| ---------------- | ------------- | ---- |
| simple_server.py | 47.94.138.231 | 2333 |
| server.py        | 47.94.138.231 | 2334 |

**Notice that these two servers are very simple and naive. If you have trouble connecting to them, it is possibly collapsed. PLEASE CONTACT WITH ME!**

### Echo Client

There are two clients in the directory `clients` corresponding to the two servers -- `simple_client.py` and `client.py`. They send your messages to the server and receive and print the response. Notice that in `client.py`, when you send **'exit'** to the server, you are then disconnected from the server.

You can use the command `python3 server.py` to run the server. If you want to set your own parameters, use the following command to get the help information. 

```
$> python client.py -h
+---------------------------------+
|                                 |
|           Echo Client           |
|                                 |
|           by DRLC (ZHZ)         |
|            zhang_hz@pku.edu.cn  |
|                                 |
+---------------------------------+


This is a simple echo client implementation.

Use the command to simply run the client:
        python3 client.py

Arguments are listed as below:
        --ip    server ip
        default value -- localhost
        --port  server port
        default value -- 2333
        --timeout       server timeout
        no timeout when negative
        default value -- -1
        --buffer        client buffer
                default value 1024
```

**Notice that simply close the console without shutting down the client process may cause some bugs on the server. PLEASE SHUT DOWN THE CLIENT BEFORE CLOSE YOUR CONSOLE!**

## Test Client

There are two more clients in the directory `clients`, and they are for testing.

`rate.py` is a client to measure the echo rate (which is corresponding to RTT). This client repeats the following procedures and calculate the echo rate. When `ctrl+C` pushed, the client stop the loop and draw a figure of the echo rate. The default path of the figure is `result/rate.jpg`.

1. Connect to the server.
2. Send a message which contains one thousand 0's.
3. Wait until receive a message.
4. Recalculate echo rate. Go to 2.

`fail_rate.py` is a client to measure the fail rate. The client repeats the following procedures and calculate the fail rate. Since TCP protocol is applied, the fail rate is actually always 0.

1. Connect to the server.
2. Send a message which contains one thousand 0's.
3. Wait until receive a message, and compare it to the original message.
4. Recalculate echo rate. Go to 2.

**Notice that simply close the console without shutting down the client process may cause some bugs on the server. PLEASE SHUT DOWN THE CLIENT BEFORE CLOSE YOUR CONSOLE!**