# This file contains the main program
from time import clock
from Socket import openSocket, sendMsg
from Init import joinedRoom, checksPING
from Settings import comDelay, comNum
from Functions import getUser, getMsg
import Commands

s = openSocket()
joinedRoom(s)

recordedChat = [""] * comNum
prevTime = 0.0
i = 0
n = 0

while True:
    # reads whatever is in the buffer and saves it to inBuffer
    inBuffer = checksPING(s)
    #print(inBuffer + "\n")
    if(inBuffer != ""):
        if(i == comNum):
            i = 0
        recordedChat[i] = getUser(inBuffer) + ": " + getMsg(inBuffer)
        i += 1
    print(recordedChat)
    # output message timing
    currentTime = clock()
    if(currentTime < prevTime):
        prevTime = 0.0
    if(currentTime - prevTime > comDelay):
        prevTime = currentTime
        # Add bot logic
        for n in range(0, comNum):
            if("hi" in recordedChat[n]):
                recordedChat = Commands.sendHi(recordedChat)
