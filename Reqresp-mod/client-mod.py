#!/usr/bin/env python3
import socket

def client_program():
    client_socket = socket.socket()
    client_socket.connect(('reqresp-server-mod', 2223))

    print("Voting options: Option A, Option B, Option C")
    print("Type 'exit' to quit")

    while True:
        vote = input("Enter your vote: ").strip()
        if vote.lower() == 'exit':
            client_socket.send(vote.encode())
            break

        client_socket.send(vote.encode())
        data = client_socket.recv(1024).decode()
        print("Server response:", data)

    client_socket.close()

if __name__ == "__main__":
    client_program()