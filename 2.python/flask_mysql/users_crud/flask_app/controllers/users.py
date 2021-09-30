from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.user import User

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    return render_template('users.html', users=User.get_all())

@app.route('/users/new')
def new():
    return render_template('new_user.html')

@app.route('/users/create', methods=['POST'])
def create():
    print(request.form)
    id = User.save(request.form)
    return redirect('/users/'+str(id))

@app.route('/users/<int:id>')
def show(id):
    data = {'id': id}
    return render_template('show_user.html', user = User.get_one(data))

@app.route('/users/<int:id>/edit')
def edit(id):
    data = {'id': id}
    return render_template('edit_user.html', user = User.get_one(data))

@app.route('/users/update', methods=['POST'])
def update():
    print(request.form)
    User.update(request.form)
    return redirect('/users')

@app.route('/users/<int:id>/delete')
def delete(id):
    data = {'id': id}
    User.delete(data)
    return redirect('/users')