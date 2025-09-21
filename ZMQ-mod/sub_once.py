#!/usr/bin/env python3
import zmq, time, sys

def main():
    ctx = zmq.Context()
    s = ctx.socket(zmq.SUB)
    s.connect("tcp://zmq-pub:12345")
    s.setsockopt_string(zmq.SUBSCRIBE, "WAKTU")
    # give publisher time (if just started)
    poller = zmq.Poller()
    poller.register(s, zmq.POLLIN)
    t_end = time.time() + 5
    while time.time() < t_end:
        socks = dict(poller.poll(500))
        if s in socks and socks[s] == zmq.POLLIN:
            msg = s.recv_string()
            print("ZMQ SUB ONCE received:", msg)
            return 0
    print("Timeout waiting for message")
    return 1

if __name__ == '__main__':
    sys.exit(main())
