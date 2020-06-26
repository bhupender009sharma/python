import socket

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECTED"
ADDR = (SERVER,PORT)

client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):                                           # this is a way to send messages
    message = msg.encode(FORMAT)                         # this is done , as we have to send messages in an encoded (or bytes ) format
    msg_length = len(message)                            # length of the message to be sent
    send_length =  str(msg_length).encode(FORMAT)        # this is done , as we have to send messages in an encoded (or bytes ) format
    # now we want to pad the send_length so it can be sended with the 64 bytes
    send_length += b' ' * (HEADER - len(send_length))       # b will denote bytes and ' ' denotes empty spaces that are going to be padded
    client.send(send_length)                                #first send length
    client.send(message)
    print(client.recv(3453).decode(FORMAT))                 #for recieving message from the server , here 3453 is just some random number, we can do the whole process of HEADER then converting it , sending its first message , then padding and bla bla blaaa....

send('bham bole')
input()                         # press enter in command prompt to to get to next commmand
send('har har mahadev')
input()
send('jai ho')
input()
send(DISCONNECT_MESSAGE)        # it will disconnect send message & then disconnect from the server

'''  to run this program from different computer , you both should be connected to same network like - wifi, or hotspot or whatever you are using.
     to run this over internet , put your PUBLIC IP ADDRESS equal to SERVER in server.py  , and then anyone can connect to you who so ever has an internet connection.
     THANKS FOR PUTTING THIS MUCH EFFORT IN READING THIS .
     I WILL SIGN OFF NOW, CHECK OUT MY GITHUB  @bhupender009sharma .
'''