#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 18:31:25 2024

@author: widhi
"""

import zmq
import random
import time
import pickle

def producer():
    context = zmq.Context()
    socket = context.socket(zmq.PUSH)
    # Bind to all interfaces on port 9999 so other containers can connect via service DNS
    socket.bind("tcp://*:9998")

    NWORKERS = 5  # Assume there are 5 workers

    while True:
        workload = random.randint(1, 100)  # Compute a random workload
        print(f"Produced workload: {workload}")
        socket.send(pickle.dumps(workload))  # Send workload to worker
        time.sleep(workload / NWORKERS)  # Balance production by waiting

producer()
