#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 18:10:24 2024

@author: widhi
"""

import zmq

def subscriber():
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    # Connect via docker compose DNS (publisher runs in zmq-pub container)
    socket.connect("tcp://zmq-pub-mod:12346")
    socket.setsockopt_string(zmq.SUBSCRIBE, "WAKTU")  # Subscribe to the TIME topic

    while True:
        message = socket.recv_string()
        print(f"Received: {message}")

subscriber()
