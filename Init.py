# This file contains the initalisation functions
import socket
from time import sleep
from Socket import sendMsg, openSocket

# this function checks that the bot successfully joins the chat
def joinedRoom(s):
    readBuffer = ""
    loading = True
    while loading:
        readBuffer = s.recv(1024).decode("utf-8")
        if("End of /NAMES list" in readBuffer):
            loading = False
    # send a message in chat to indicate that the bot has successfully joined
    sendMsg(s, "HeyGuys")

# this function check to see if the server sent a PONG. if a PONG is detected,
# a PING is sent back to the server and 0 is returned. Otherwise, the function
# passes the message read back. Now the function also re-establishes a
# connection with the server if the connection drops.
def checksPING(s):
    readBuffer = ""
    # set socket timeout
    s.settimeout(0.1)
    try:
        readBuffer = s.recv(1024).decode("utf-8")
    except socket.timeout as e:
        return ""
    except socket.error as e:
        print(e)
        sys.exit(1)
    else:
        # recieved a buffer input
        if len(readBuffer) == 0:
            t = 10
            print("Server shutdown occured, reconnecting in " + str(t) + "S")
            sleep(t)
            return "RESTART_CONNECTION"
        elif("PING :tmi.twitch.tv" in readBuffer):
            print("PING recieved")
            s.send((readBuffer.replace("PING", "PONG")).encode())
            print("PONG sent")
            return ""
        else:
            return readBuffer
