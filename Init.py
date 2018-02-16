from Socket import sendMsg

# this function checks that the bot successfully joins the chat
def joinedRoom(s):
    readBuffer = ""
    loading = True

    while loading:
        readBuffer = readBuffer + str(s.recv(1024))
        if("End of /NAMES list" in readBuffer):
            loading = False


    # send a message in chat to indicate that the bot has successfully joined
    sendMsg(s, "Great success!")
