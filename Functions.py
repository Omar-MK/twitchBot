def getUser(feed):
    seperated = feed.split(":", 2)
    user = seperated[1].split("#", 1)[1].replace(" ", "")
    return user

def getMsg(feed):
    seperated = feed.split(":", 2)
    msg = seperated[2].replace("\r\n", "")
    return msg
