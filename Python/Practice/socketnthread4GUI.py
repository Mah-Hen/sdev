import socket
import threading
import time

port = 17226 # Destination's port
serverAddress = ('localhost', 48000)


def receive_message(clientSocket, username):
    clientSocket.settimeout(30)
    while True:
        try:
            message = clientSocket.recv(1024).decode()
            print(f"\n{username} received {message}")
            if not message:
                break
        except socket.timeout:
            #print("ERROR!\nTimeout occured while waiting for response...")
            print("\nFrom Server; Timeout Error!\nDisconnecting...")
            clientSocket.close()
            break
    
def send_message(destAddress, username):
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        message = input("\nMessage:")
        clientSocket.sendto(message.encode(), destAddress)
        if len(message) == 0:
            print("\nDisconnecting...")
            break

# Get client's username
username = input("Enter username: ")


'''Create a UDP socket and bind to username and port'''
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSocket.bind((username, port)) 

'''Get the address of the other client'''
destUsername = input("Enter username of destination:")
destAddress = (destUsername, serverAddress[1])   # 48000

#Start receiving thread
receiveThread = threading.Thread(target=receive_message, args=(clientSocket, username))
receiveThread.start()

#Start sending thread
sendThread = threading.Thread(target=send_message, args=(destAddress, username))
sendThread.start()

#Wait for threads to finish
sendThread.join()
receiveThread.join()

#Close the socket
clientSocket.close()

