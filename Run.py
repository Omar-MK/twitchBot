# This file contains the main program
import Commands
from time import clock
from Socket import openSocket, sendMsg
from Init import joinedRoom, checksPING
from Settings import outputDelay, commentNum
from Functions import getUser, getMsg

s = openSocket()
joinedRoom(s)

recordedChat = [""] * commentNum
prevTime = 0.0
i = 0
n = 0

while True:
    # reads whatever is in the buffer and saves it to inBuffer
    inBuffer = checksPING(s)
    # if nothing is in the buffer, don't add anything to recordedChat
    if(inBuffer == ""):
        pass
    # if RESTART_CONNECTION is passed back to inBuffer, restart the connection
    # to the server
    elif(inBuffer == "RESTART_CONNECTION"):
        s = openSocket()
        joinedRoom(s)
    # otherwise just add the message contained in inBuffer to recordedChat 
    else:
        if(i == commentNum):
            i = 0
        recordedChat[i] = getUser(inBuffer) + ": " + getMsg(inBuffer)
        i += 1
    # output message timing
    currentTime = clock()
    if(currentTime < prevTime):
        prevTime = 0.0
    if(currentTime - prevTime > outputDelay):
        prevTime = currentTime
        # Add bot logic
        for n in range(0, commentNum):
            if("hi" in recordedChat[n]):
                recordedChat = Commands.sendHi(recordedChat)
