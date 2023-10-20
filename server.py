import socket

# Create a socket instance and pass it two parameters
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = socket.gethostname()  # get the local hostname
port = 60000  # initiate port
payload_size = 2048
s.bind((host, port))  # bind host address and port together
print('Server listening....')

while True:
    print("Waiting to receive message from client...")
    data, addr = s.recvfrom(payload_size)  # Read from UDP socket into data
    ReceivedMessage = data.decode()  # Receive the filename from the client
    print("Received filename from Client: %s" % ReceivedMessage)
    fileName = repr(ReceivedMessage)
    fileNameS = fileName.strip('\'')
    f = open(fileNameS, 'rb')  # open file
    l = f.read(payload_size)

    # send file data to client
    if l:
        sent = s.sendto(l, addr)
        print('Sent \n', sent)
    f.close()  # close file
    print('Closing connection to the server')
    s.close()  # close connection

