#!/usr/bin/env python3
import zmq
import pickle
import sys
import time

def worker(id):
    context = zmq.Context()
    socket = context.socket(zmq.PULL)
    socket.connect("tcp://zmq-push-mod:9998")

    while True:
        task = pickle.loads(socket.recv())
        workload = task["workload"]

        if task["priority"] == "High":
            factor = 0.5
        elif task["priority"] == "Medium":
            factor = 1
        else:
            factor = 1.5

        print(f"Worker {id} mengerjakan {task['type']} task "
              f"({task['priority']} priority, workload={workload})")
        time.sleep(workload * factor)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python pull_worker_task_types.py <worker_id>")
        exit(1)
    worker_id = sys.argv[1]
    worker(worker_id)
