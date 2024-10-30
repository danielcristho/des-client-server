import socket
import library
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Client has started")


def validate_input(user_input):
    if not user_input:
        logging.warning("Input cannot be empty")
        return False
    return True


def authenticate(mySocket):
    while True:
        username_prompt = mySocket.recv(1024).decode()
        print(username_prompt)
        username = input("Your username: ")
        mySocket.send(username.encode())

        password_prompt = mySocket.recv(1024).decode()
        print(password_prompt)
        password = input("Your password: ")
        mySocket.send(password.encode())

        response = mySocket.recv(1024).decode().strip()
        print(f"Server response: {response}")

        if response == "Authentication successful.":
            break
        else:
            print("Authentication failed, please try again.\n")


def main():
    host = "127.0.0.1"
    port = 5000
    mySocket = socket.socket()
    mySocket.connect((host, port))

    authenticate(mySocket)

    message = input("#client -> ")

    while message != "q":
        if validate_input(message):
            logging.info(f"Input received: {message}")
            finalEncryptedMessage = library.encrypt(message)
            mySocket.send(finalEncryptedMessage.encode())
            library.sending()
            print("\nEncrypted message = " + finalEncryptedMessage)

            data = mySocket.recv(1024).decode()
            print("Received from server = " + data)

            decryptedMessage = library.decrypt(data)
            if not data:
                break
            print("Decrypted Message = " + str(decryptedMessage))
            print("\n")
        else:
            logging.error("Invalid input, please try again.")

        message = input("Enter the message you want to encrypt -> ")

    mySocket.close()


if __name__ == "__main__":
    main()
