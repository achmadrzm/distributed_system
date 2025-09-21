#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 09:19:10 2024

@author: widhi
"""

import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
# Connect using docker service DNS name of the REP server
socket.connect("tcp://zmq-rep-mod:5556")

for request in range(1):
    print(f"Sending request {request} ...")
    socket.send(b"Hello")
    message = socket.recv()
    print(f"Received reply {request}: {message}")
