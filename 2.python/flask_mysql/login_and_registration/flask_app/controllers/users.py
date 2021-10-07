from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_bcrypt import Bcrypt
from flask_app.models.user import User
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    if not User.validate_user(request.form):
        return redirect('/')
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': bcrypt.generate_password_hash(request.form['password'])
    }
    id = User.save(data)
    session['id'] = id
    return redirect('/dashboard')

@app.route('/login', methods=['POST'])
def login():
    user = User.get_by_email(request.form)
    if not user:
        flash('Invalid email.', 'login')
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash('Password is incorrect.', 'login')
        return redirect('/')
    session['id'] = user.id
    return redirect('/dashboard')
    

@app.route('/dashboard')
def dashboard():
    if 'id' not in session:
        return redirect('/')
    data = {'id': session['id']}
    user = User.get_by_id(data)
    return render_template('dashboard.html', user=user)

@app.route('/logout')
def logout():
    session.pop('id')
    return redirect('/')
