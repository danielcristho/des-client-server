import socket
import des
import library

#this will serve as the "server" for our implementation

def Main():
    host = "127.0.0.1"
    port = 5001
    #necessary to initiate the server
    mySocket = socket.socket()
    mySocket.bind((host,port))

    print("Waiting for connection.....")
    #listens for a user to connect
    mySocket.listen(2)
    #getting the user's connection info
    conn, addr = mySocket.accept()
    print ("Connection from: " + str(addr))

    while True:
            #receiving the response from the other user
            data = conn.recv(1024).decode()
            print("Received from client = " + data)
            #decrypting the other user's message
            decryptedMessage = library.decrypt(data)
            if not data:
                    break
            print ("Decrypted Message = " + str(decryptedMessage))
            print("\n")
            message = input("Enter the message you want to encrypt -> ")
            #encrypting the message using DES
            finalEncryptedMessage = library.encrypt(message)
            print("Encrypted message = " + finalEncryptedMessage)
            #prints the pretty loading bar
            library.sending()
            #sending the message
            conn.send(finalEncryptedMessage.encode())

    conn.close()

if __name__ == '__main__':
    Main()