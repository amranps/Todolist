from flask import Flask, render_template, request, redirect, url_for, abort


app = Flask(__name__)


todos = [
    {'id': 1, 'task': 'Learn Flask'},
    {'id': 2, 'task': 'Build a project'},
    {'id': 3, 'task': 'Deploy the app'},
]


next_id = 4




# Homepage: display all tasks
@app.route('/')
def get_todos():
    return render_template('todos.html', todos=todos)




# Add a new task
@app.route('/add', methods=['POST'])
def add_todo():
    global next_id


    task = request.form.get('task', '').strip()


    if task:
        todos.append({
            'id': next_id,
            'task': task
        })


        next_id += 1


    return redirect(url_for('get_todos'))




# Edit an existing task
@app.route('/edit/<int:todo_id>', methods=['GET', 'POST'])
def edit_todo(todo_id):
    todo = next(
        (item for item in todos if item['id'] == todo_id),
        None
    )


    if todo is None:
        abort(404)


    if request.method == 'POST':
        task = request.form.get('task', '').strip()


        if task:
            todo['task'] = task


        return redirect(url_for('get_todos'))


    return render_template('edit.html', todo=todo)




# Delete a task
@app.route('/delete/<int:todo_id>', methods=['POST'])
def delete_todo(todo_id):
    global todos


    todos = [
        item for item in todos
        if item['id'] != todo_id
    ]


    return redirect(url_for('get_todos'))




# Run the application
if __name__ == '__main__':
    app.run(debug=True)