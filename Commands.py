# This file should contain the commands the bot will respond to in chat
# a more efficent implementation will replace this approach soon.
from Socket import openSocket, sendMsg

def sendHi(chatArray):
    for n in range (0, len(chatArray)):
        chatArray[n] = ""
    sendMsg(openSocket(), "HeyGuys")
    return chatArray
