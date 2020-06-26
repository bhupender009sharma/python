# TO RUN THIS PROGRAM->
#RUN SERVER  EITHER FROM IDE OR FROM TERMINAL (FOR TERMINAL GO TO PROJECT'S DIRECTORY BY USING (e.g.  C:\Users\acer\PycharmProjects\socket_program) AND )
# THEN ENTER COMMAND  python server.py
# for running number of clients open same number of terminals  and enter command   python client.py


import socket           # used for socket side of work
import threading        # used for running multiple programs , without waiting for earlier program to finish first

# CAPITAL variables will be constant here
HEADER = 64         #it is going to tell us what .. the first message from the server to every single time from the client is going to be a header of length 64, that gonna tell us the length of the message that's gonna come next
# since we dont know the length of the message that is going to come, so every single time needs to be a message of length 64
# these 64 bytes will have a number in them that tell ud the number of bytes we are about to recieve.

PORT = 5050             # can choose any port , in a range

#SERVER = "192.168.43.86"    # server address, here ip address of my own IP , as i am using it as a server
SERVER = socket.gethostbyname(socket.gethostname())      # this automatically get my ip, bcoz if i am using it on another pc , then i have to change it to another, then i have to change it again. So now , i dont need to the above line
# gethostname gives us the name of our computer , and gethostbyname gives our ip address, try it by printing these two commands, if you can
# now we have to create a socket , which is going to allow us to open this server to other devices.
# the first step is to pick the port  and pick the server ,and then pick the socket and then bind the socket to that address

ADDR = (SERVER,PORT)
FORMAT = 'utf-8'                                                  # utf-8 a decoding method from bytes from
DISCONNECT_MESSAGE  = "!DISCONNECTED"                             # when we recieved this message we are going to close the connection and disconnect the client


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        # socket.socket is how we create a new socket and the argument os actually the family of the socket that we want to. Family is a kind of category, and there are a lot of different categories that we can pick
# and they are genrally prefixed with AF. INET tells that what kind of IP address we are going to be looking for specific connections , INET_6 resembles to IPv4 ....and so on
#SOCK_STREAM means that we are streaming data through the different ways of sending data through the socket

server.bind(ADDR)                                                 # it means we have bound the socket to the address ADDR, and anything that hits the address will hit to the socket

def handle_client(conn, addr):                                    # conn = connection, addr= address, it will handlw individual connections b/w the client and server
    # this function will be running concurrently for each client
    print(f"[NEW CONNECTION] {addr} connected.")                  # this will tell us who gets connected
    connected = True
    while connected:                                              # here we will wait till the client is not connected, and when connected then we going to do something with it in this loop
        msg_length = conn.recv(HEADER).decode()                   # in recv we have to specify how many bytes we are going to recieve, read HEADER comments above to understand it, and then decode it from bytes format using utf-8
        # the above type of line is called blocking line , which means we are not going to pass this line of code until we recieve some kind of message from our client. it is necessary so that we are not blocking other clients
        if msg_length:
            msg_length = int(msg_length)                          # converting message length from
            msg = conn.recv(msg_length).decode(FORMAT)            # first message tells us how long is message that is coming , and this one tell us how many we are going to be recieving for actual message
            # if the client disconnect from the server directly without safe method from the server, it will get disconnected , but the problem will occur if the client tries to connect again then the server will show it is already connected. so we are creating the following function for proper disconnection
            if msg == DISCONNECT_MESSAGE:                         #this will disconnect the client from the server.
                connected = False

            print(f"[{addr}] {msg}")                              # addr =  client , msg =  what it send
            conn.send("msg recieved".encode(FORMAT))              # message sent from the server side to the client

    conn.close()                                                  # it will close the connection

def start():                                                      #it will handle new connections , where they need to go
    server.listen()                                               # it means we are listening for new connections
    print(f"[LISTENING] server is listening on {SERVER}")         #it will tell us on which IP address server is running on
    while True:
        conn, addr = server.accept()                                          # server.accept() is going to wait for new connection , when new connection comes addr will store connection's address and conn will store it as an object, so as to use it to send data back and forth
        thread = threading.Thread(target=handle_client,args=(conn,addr))      # target - is the function to call for threading and args are the arguments to pass through it
        thread.start()                                                        #start thrading
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount()-1}")            # it will tell us how many active connections are there on the server, as on is always running i.e. start function so -1

print("[STARTING] server is starting ......")
start()