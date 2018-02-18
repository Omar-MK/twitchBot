from Socket import openSocket, sendMsg

def sendHi(chatArray):
    for n in range (0, len(chatArray)):
        chatArray[n] = ""
    sendMsg(openSocket(), "HeyGuys")
    return chatArray
