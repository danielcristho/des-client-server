import socket
import library
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Server has started")


def validate_input(user_input):
    if not user_input:
        logging.warning("Input can't be empty.")
        return False
    return True


valid_credentials = {"daniel": "tc20", "riyanda": "tc22"}


def validate_credentials(username, password):
    return valid_credentials.get(username) == password


def main():
    host = "127.0.0.1"
    port = 5000
    mySocket = socket.socket()
    mySocket.bind((host, port))

    print("Waiting for connection...")
    mySocket.listen(2)
    conn, addr = mySocket.accept()
    print("Connection from:", addr)

    while True:
        conn.send("Enter your username: ".encode())
        username = conn.recv(1024).decode()
        conn.send("Enter your password: ".encode())
        password = conn.recv(1024).decode()

        logging.info(f"Username: {username}, Password: {password}")

        if validate_credentials(username, password):
            logging.info("User authenticated successfully.")
            conn.send("Authentication successful.".encode())
            break
        else:
            logging.warning("Authentication failed.")
            conn.send("Authentication failed. Please try again.".encode())

    while True:
        data = conn.recv(1024).decode()
        if not data:
            logging.warning("No data received from client, closing connection.")
            break
        print("\nReceived from client =", data)

        decryptedMessage = library.decrypt(data)
        # Decrypt user's message
        print("Decrypted Message =", decryptedMessage)
        print("\n")
        """
        Send message & encrypt the message
        """
        while True:
            message = input("#server -> ")
            if validate_input(message):
                logging.info(f"Input received: {message}")
                finalEncryptedMessage = library.encrypt(message)
                print("Encrypted message =", finalEncryptedMessage)

                library.sending()
                conn.send(finalEncryptedMessage.encode())
                break
            else:
                logging.error("Invalid input, please try again.\n")

    conn.close()


if __name__ == "__main__":
    main()
