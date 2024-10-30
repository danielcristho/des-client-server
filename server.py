import socket
import library

def main():
    host = "127.0.0.1"
    port = 5001
    mySocket = socket.socket()
    mySocket.bind((host, port))

    print("Waiting for connection...")
    mySocket.listen(2)
    conn, addr = mySocket.accept()
    print("Connection from:", addr)

    while True:
        data = conn.recv(1024).decode()
        print("Received from client =", data)

        decryptedMessage = library.decrypt(data)
        if not data:
                break
        # Decrypt user's message
        print("Decrypted Message =", decryptedMessage)
        print("\n")
        """
        Send message & encrypt the message
        """
        message = input("#server -> ")
        finalEncryptedMessage = library.encrypt(message)
        print("Encrypted message =", finalEncryptedMessage)

        library.sending()
        conn.send(finalEncryptedMessage.encode())

    conn.close()

if __name__ == '__main__':
    main()
