#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 18:32:02 2024

@author: widhi
"""

import zmq
import time
import pickle

def worker(id):
    context = zmq.Context()
    socket = context.socket(zmq.PULL)
    # Connect to the push producer container by its service name (defined in docker compose)
    socket.connect("tcp://zmq-push-mod:9998")

    while True:
        work = pickle.loads(socket.recv())  # Receive work from producer
        print(f"Worker {id} received work: {work}")
        time.sleep(work)  # Simulate doing work

if __name__ == "__main__":
    worker(1)  # Start a worker with an ID of 1
