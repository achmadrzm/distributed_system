#!/usr/bin/env python3
import requests

BASE = 'http://rest-server-mod:5152'

def list_tasks():
    r = requests.get(f"{BASE}/tasks")
    print(r.json())

def add_task(title):
    r = requests.post(f"{BASE}/tasks", json={'title': title})
    print(r.json())

def update_task(task_id, title=None, done=None):
    data = {}
    if title: data['title'] = title
    if done is not None: data['done'] = done
    r = requests.put(f"{BASE}/tasks/{task_id}", json=data)
    print(r.json())

def delete_task(task_id):
    r = requests.delete(f"{BASE}/tasks/{task_id}")
    print(r.json())

if __name__ == '__main__':
    # contoh penggunaan
    add_task("Belajar Docker")
    add_task("Implement REST API")
    list_tasks()
    update_task(1, done=True)
    delete_task(2)
    list_tasks()