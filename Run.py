from Socket import openSocket
from Init import joinedRoom

s = openSocket()
joinedRoom(s)

while True:
    running = True
