import socket
import threading
from datetime import datetime

def handle_client(my_socket, client_address):
    try:
        # Request username
        my_socket.send("Enter your username: ".encode('utf-8'))
        username = my_socket.recv(1024).decode('utf-8').strip()
        print(f"\033[92mUser '{username}' connected from {client_address}\033[0m")
        
        # Logging setup
        log_file = open(f"chat_log_{username}.txt", 'a')
        
        def log(sender, message):
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_file.write(f"[{timestamp}] {sender}: {message}\n")
        
        def receive():
            while True:
                try:
                    data = my_socket.recv(1024).decode('utf-8')
                    if not data:
                        break
                    timestamp = datetime.now().strftime("%H:%M:%S")
                    print(f'\033[94m[{timestamp}] {username}: {data}\033[0m')
                    log(username, data)
                    if data.lower() == 'bye':
                        my_socket.close()
                        break
                except:
                    break

        def send():
            while True:
                try:
                    msg = input()
                    timestamp = datetime.now().strftime("%H:%M:%S")
                    my_socket.send(msg.encode('utf-8'))
                    print(f'\033[93m[{timestamp}] You: {msg}\033[0m')
                    log("Server", msg)
                    if msg.lower() == 'bye':
                        my_socket.close()
                        break
                except:
                    break

        receive_thread = threading.Thread(target=receive)
        send_thread = threading.Thread(target=send)
        
        receive_thread.start()
        send_thread.start()
        
        receive_thread.join()
        send_thread.join()
        
    except Exception as e:
        print(f"\033[91mError: {e}\033[0m")
    finally:
        log_file.close()
        my_socket.close()
        print(f"\033[91mConnection with {username} closed.\033[0m")

def main():
    s = socket.socket()
    s.bind(('127.0.0.1', 2040))
    s.listen()
    print("\033[95mServer is listening on port 2040...\033[0m")
    while True:
        my_socket, client_address = s.accept()
        client_thread = threading.Thread(target=handle_client, args=(my_socket, client_address))
        client_thread.start()

if __name__ == "__main__":
    main()