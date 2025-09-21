#!/usr/bin/env python3
import zmq
import time
import random
import pickle

def producer():
    context = zmq.Context()
    socket = context.socket(zmq.PUSH)
    socket.bind("tcp://*:9998")

    task_types = ["Compute", "IO", "Network"]
    priorities = ["High", "Medium", "Low"]

    while True:
        task = {
            "type": random.choice(task_types),
            "priority": random.choice(priorities),
            "workload": random.randint(1, 5)
        }
        print(f"Producer mengirim: {task}")
        socket.send(pickle.dumps(task))
        time.sleep(0.5)

if __name__ == "__main__":
    producer()
