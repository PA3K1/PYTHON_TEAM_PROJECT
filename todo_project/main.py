from flask import Flask, request, render_template

app = Flask(__name__)

# Три списка: активные, выполненные и удаленные задачи
active_tasks = []
completed_tasks = []
deleted_tasks = []

@app.route('/')
def index():
    return render_template('index.html',
                         active_tasks=active_tasks,
                         completed_tasks=completed_tasks,
                         deleted_tasks=deleted_tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form['task']
    active_tasks.append(task)
    print(f"Добавлена задача: {task}")
    return index()

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(active_tasks):
        # Перемещаем задачу из активных в удаленные
        deleted_task = active_tasks.pop(task_id)
        deleted_tasks.append(deleted_task)
        print(f"Задача удалена: {deleted_task}")
    return index()

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    if 0 <= task_id < len(active_tasks):
        # Перемещаем задачу из активных в выполненные
        completed_task = active_tasks.pop(task_id)
        completed_tasks.append(completed_task)
        print(f"Задача выполнена: {completed_task}")
    return index()

@app.route('/edit/<int:task_id>', methods=['POST'])
def edit_task(task_id):
    if 0 <= task_id < len(active_tasks):
        new_text = request.form['edited_task']
        active_tasks[task_id] = new_text
        print(f"Задача изменена: {new_text}")
    return index()

if __name__ == '__main__':
    app.run(debug=True)