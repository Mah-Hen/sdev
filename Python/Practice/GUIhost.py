import tkinter as tk
import socket
import threading

class GUIhost:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Chat Client")

        # Initialize Graphical Interface
        #Connection Parameters Entry n Label
        self.sourcePort = tk.Entry(self.window, font=("Calibri",12))
        self.sourcePortLabel = tk.Label(self.window, text="Source Port", font=("Calibri",12))
        self.destinationIP = tk.Entry(self.window, font=("Calibri",12))
        self.destinationIPLabel = tk.Label(self.window, text="Destination IP", font=("Calibri",12))
        self.destinationPort = tk.Entry(self.window, font=("Calibri",12))
        self.destinationPortLabel = tk.Label(self.window, text="Destination Port", font=("Calibri",12))
        self.nameEntry = tk.Entry(self.window, font=("Calibri",12))
        self.nameLabel = tk.Label(self.window, text="Name", font=("Calibri",12))

        #Message Display
        self.messageDisplay = tk.Text(self.window, state=tk.DISABLED) #makes this not interactive 

        #Entry and Button
        self.messageEntry = tk.Entry(self.window, font="Calibri")
        self.sendButton = tk.Button(self.window, text="Send", command=self.sendMessage)

        #Layout
        self.nameEntry.grid(row=0,column=0, sticky='w')
        self.nameLabel.grid(row=0,column=1)
        self.sourcePort.grid(row=1,column=0, sticky='w')
        self.sourcePortLabel.grid(row=1,column=1)
        self.destinationPort.grid(row=2,column=0, sticky='w')
        self.destinationPortLabel.grid(row=2,column=1)
        self.destinationIP.grid(row=3,column=0, sticky='w')
        self.destinationIPLabel.grid(row=3,column=1)
        self.messageEntry.grid(row=5,column=0)
        self.messageDisplay.grid(row=4,column=0, columnspan=2)
        self.sendButton.grid(row=5, column=1)
        


        #Initialize socket and thread
        self.socket = None
        self.receiveThread = None

    def start(self):
        self.window.mainloop() 

    def setConnection(self):
        self.name = self.nameEntry.get()
        self.sourcePort = int(self.sourcePort.get())
        self.destinationIP = self.destinationIP.get()
        self.destinationPort = int(self.destinationPort.get())
        print(type(self.name))
        print(type(self.sourcePort))
        print(type(self.destinationPort))
        print(type(self.destinationIP))

        # initialize connection
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(("127.0.0.1", self.sourcePort))
        self.socket.settimeout(30)
        # receiving messages thread 
        self.receiveThread = threading.Thread(target=self.receiveMessages)
        self.receiveThread.start()
        
    def receiveMessages(self):
        while True:
            try:
                data, addr = self.rocket.recvfrom(1024)
                message = data.decode()
                self.messageDisplay.configure(state=tk.NORMAL)
                self.messageDisplay.insert(tk.END, message)
                self.messageDisplay.configure(state=tk.DISABLED)
            except:
                break

    def sendMessage(self):
        message = self.messageEntry.get()
        if message:
            message = self.name + ": " + message + "\n"
            self.socket.sendto(message.encode(), (self.destinationIP, self.destinationPort))
            self.messageDisplay.configure(state=tk.NORMAL)
            self.messageDisplay.insert(tk.END, message)
            self.messageDisplay.configure(state=tk.DISABLED)
            self.messageEntry.delete(0, tk.END)

if __name__ == "__main__":
    client = GUIhost()
    connectButton = tk.Button(client.window, text="Connect", command= client.setConnection)
    connectButton.grid(row=6, column=0, columnspan=2)
    client.start()


#Socket and Threading
'''
Entry
entryLabel = tk.Text(root, height = 1, width=100,  font=("Calibri"))
entryLabel.grid(row=0, column=0, sticky='w')

entryLabel.bind("<Return>", getText)

Textbox
textbox = ScrolledText(root, height=9, width=40, font=("Calibri"))
textbox.grid(row=1, column=0, sticky='nw')

Listening Port
listLabel = tk.Label(frame, text='Listening Port', font=("Calibri", "12", 'bold'))
listLabel.grid(row=2, column=0, sticky='w')

listEntry = tk.Entry(frame, font=("Calibri"), width=12)
listEntry.grid(row=2, column=1, sticky='w')

Destination Port
destLabel = tk.Label(frame, text='Destination Port', font=("Calibri", "12", 'bold'))
destLabel.grid(row=3, column=0, sticky='W')

destEntry = tk.Entry(frame, font=("Calibri"), width=12)
destEntry.grid(row=3, column=1, sticky='w')

Destination IP
IPLabel = tk.Label(frame, text='Destination IP', font=("Calibri", "12", 'bold'))
IPLabel.grid(row=4, column=0, sticky='W')

IPEntry = tk.Entry(frame, font=("Calibri"), width=12)
IPEntry.grid(row=4, column=1, sticky='w')

Name
nameLabel = tk.Label(frame, text='Name', font=("Calibri", "12", 'bold'))
nameLabel.grid(row=5, column=0, sticky='W')

nameEntry = tk.Entry(frame, font=("Calibri"), width=12)
nameEntry.grid(row=5, column=1, sticky='w')


nameEntry.bind("<Return>", getText)


frame.grid(sticky='w')
root.mainloop()

# Get client's username
IPEntry.bind("<Return>", getText)
destEntry.bind("<Return>", getText)
listEntry.bind("<Return>", getText)



#Create a UDP socket and bind to username and port
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSocket.bind((username, port)) 

#Get the address of the other client
destUsername = input("Enter username of destination:")
destAddress = (destIP, serverAddress[1])   # 48000

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
'''


    