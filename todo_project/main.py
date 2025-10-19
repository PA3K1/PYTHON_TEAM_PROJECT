from flask import Flask, request, render_template

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form['task']
    tasks.append(task)
    print(f"Добавлена задача: {task}")
    print(f"Все задачи: {tasks}")
    return index()

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        removed_task = tasks.pop(task_id)
        print(f"Удалена задача: {removed_task}")
        print(f"Остались задачи: {tasks}")
    return index()

if __name__ == '__main__':
    app.run(debug=True)