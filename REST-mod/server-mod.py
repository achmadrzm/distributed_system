#!/usr/bin/env python3
from flask import Flask, request, jsonify

app = Flask(__name__)

# Simpan tasks dalam memory
tasks = {}
next_id = 1

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    global next_id
    data = request.json
    if not data or 'title' not in data:
        return jsonify({'error': 'Missing title'}), 400
    task_id = next_id
    tasks[task_id] = {'title': data['title'], 'done': False}
    next_id += 1
    return jsonify({'id': task_id, 'task': tasks[task_id]}), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    if task_id not in tasks:
        return jsonify({'error': 'Task not found'}), 404
    data = request.json
    tasks[task_id]['title'] = data.get('title', tasks[task_id]['title'])
    tasks[task_id]['done'] = data.get('done', tasks[task_id]['done'])
    return jsonify({'id': task_id, 'task': tasks[task_id]})

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    if task_id not in tasks:
        return jsonify({'error': 'Task not found'}), 404
    del tasks[task_id]
    return jsonify({'message': f'Task {task_id} deleted'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5152)