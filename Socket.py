# This file contains all the functions that are used to interact with the socket
# import the socket class so we could use the socket fuctions
import socket
from Settings import HOST, PORT, PASS, NICK, CHANNEL

# this function opens the socket and sends the bot nickname
def openSocket():
    # open the socket to connect to the chat

    # create a socket
    s = socket.socket()
    # connect to the port
    s.connect((HOST, PORT))
    # send password to login
    s.send(("PASS " + PASS + "\r\n").encode())
    # send the bot nickname
    s.send(("NICK " + NICK + "\r\n").encode())
    # join the chat room
    s.send(("JOIN #" + CHANNEL + "\r\n").encode())
    return s


# this fucntion sends a message sent through the socket
# input (socket_name, message)
def sendMsg(s, msg):
    s.send(("PRIVMSG #" + CHANNEL  + " :" + msg + "\r\n").encode())
    print("Sent to " + CHANNEL + "'s chat: " + msg)
