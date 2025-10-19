from flask import Flask, request, render_template

app = Flask(__name__)

# Два списка: обычные задачи и выполненные
tasks = []
completed_tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks, completed_tasks=completed_tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form['task']
    tasks.append(task)
    print(f"Добавлена задача: {task}")
    return index()

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        removed_task = tasks.pop(task_id)
        print(f"Удалена задача: {removed_task}")
    return index()

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    if 0 <= task_id < len(tasks):
        # Перемещаем задачу из tasks в completed_tasks
        completed_task = tasks.pop(task_id)
        completed_tasks.append(completed_task)
        print(f"Задача выполнена: {completed_task}")
    return index()

if __name__ == '__main__':
    app.run(debug=True)