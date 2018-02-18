# This file contains the initalisation functions
from Socket import sendMsg

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
# passes the message read back
def checksPING(s):
    readBuffer = ""
    readBuffer = s.recv(1024).decode("utf-8")
    if("PING :tmi.twitch.tv" in readBuffer):
        s.send((readBuffer.replace("PING", "PONG")).encode())
        print("PING sent to server")
        return ""
    else:
        return readBuffer
