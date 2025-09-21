#!/usr/bin/env python3
import socket

# Inisialisasi vote count
votes = {"Option A": 0, "Option B": 0, "Option C": 0}

def server_program():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 2223))
    server_socket.listen(1)
    print("Polling Server listening on port 2223")

    conn, addr = server_socket.accept()
    print(f"Connection from: {addr}")

    while True:
        data = conn.recv(1024).decode()
        if not data:
            print("Client disconnected")
            break

        vote = data.strip()
        if vote.lower() == "exit":
            print("Client requested exit")
            break

        if vote in votes:
            votes[vote] += 1
            response = f"Vote received for {vote}, current count: {votes[vote]}"
        else:
            response = f"Invalid option. Available: {', '.join(votes.keys())}"

        conn.send(response.encode())

    conn.close()
    print("Server stopped")

if __name__ == "__main__":
    server_program()