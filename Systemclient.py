import socket
import threading
from datetime import datetime

def receive_messages(sock, username):
    while True:
        try:
            msg = sock.recv(1024).decode('utf-8')
            if not msg:
                break
            timestamp = datetime.now().strftime("%H:%M:%S")
            print(f'\033[94m[{timestamp}] Server: {msg}\033[0m')
            if msg.lower() == 'bye':
                sock.close()
                break
        except Exception as e:
            print(f"\033[91mConnection closed.\033[0m")
            break

def send_messages(sock, username):
    while True:
        try:
            data = input()
            timestamp = datetime.now().strftime("%H:%M:%S")
            sock.send(data.encode('utf-8'))
            print(f'\033[92m[{timestamp}] You: {data}\033[0m')
            if data.lower() == 'bye':
                break
        except Exception as e:
            print(f"\033[91mError sending message.\033[0m")
            break

def main():
    s = socket.socket()
    try:
        s.connect(('127.0.0.1', 2040))
        # Get username prompt
        username_prompt = s.recv(1024).decode('utf-8')
        username = input(username_prompt)
        s.send(username.encode('utf-8'))
        
        # Start threads
        receive_thread = threading.Thread(target=receive_messages, args=(s, username))
        send_thread = threading.Thread(target=send_messages, args=(s, username))
        
        receive_thread.start()
        send_thread.start()
        
        receive_thread.join()
        send_thread.join()
        
    except Exception as e:
        print(f"\033[91mError: {e}\033[0m")
    finally:
        s.close()

if __name__ == "__main__":
    main()