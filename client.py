import socket
import library

def main():
    host = "127.0.0.1"
    port = 5001
    mySocket = socket.socket()
    mySocket.connect((host, port))

    message = input("#client -> ")
    finalEncryptedMessage = library.encrypt(message)
    print("Encrypted message = " + finalEncryptedMessage)

    while message != 'q':
        library.sending()
        finalEncryptedMessage = library.encrypt(message)
        mySocket.send(finalEncryptedMessage.encode())

        data = mySocket.recv(1024).decode()
        print("Received from server = " + data)

        decryptedMessage = library.decrypt(data)
        if not data:
                break
        print("Decrypted Message = " + str(decryptedMessage))
        print("\n")

        message = input("Enter the message you want to encrypt -> ")
        finalEncryptedMessage = library.encrypt(message)
        print("Encrypted message = " + finalEncryptedMessage)

    mySocket.close()

if __name__ == '__main__':
        main()
