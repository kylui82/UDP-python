import socket

# Create a socket instance and pass it two parameters
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = socket.gethostname()  # get the local hostname
port = 60000  # initiate port
payload_size = 2048 # initiate port size
server_address = (host, port)
try:
    print("Connecting to %s port %s" % server_address)
    file_name = 'mytext.txt'.encode()  # filename of request file
    s.sendto(file_name, (host, port))  # send the filename to the server
    print("Sending filename %s ..." % file_name.decode())
    data, server_addr = s.recvfrom(payload_size)  # Read data from UDP socket into data
    Recv_Message = data.decode()
    print('Received message: \n', Recv_Message)  # print out received string

finally:
    s.close()  # close connection
    print('connection closed')