from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.recipe import Recipe
from flask_app.models.user import User

@app.route('/recipes/new')
def add_new():
    if 'id' not in session:
        return redirect('/')
    return render_template('add_new.html')

@app.route('/create', methods=['POST'])
def create():
    if not Recipe.validate_recipe(request.form):
        return redirect('/recipes/new')
    data = {
        'name': request.form['name'],
        'description': request.form['description'],
        'under_30_minutes': request.form['under_30_minutes'],
        'instructions': request.form['instructions'],
        'date_made': request.form['date_made'],
        'user_id': session['id']
    }
    print(data)
    Recipe.save(data)
    return redirect('/dashboard')

@app.route('/recipes/delete/<int:id>')
def delete(id):
    data = {'id': id}
    Recipe.delete(data)
    return redirect('/dashboard')

@app.route('/recipes/<int:id>')
def display(id):
    if 'id' not in session:
        return redirect('/')
    data = {'id': id}
    recipe = Recipe.get_one(data)
    return render_template('/display.html', recipe=recipe, user_name=session['name'] )

@app.route('/recipes/edit/<int:id>')
def edit(id):
    if 'id' not in session:
        return redirect('/')    
    data = {'id': id}
    recipe = Recipe.get_one(data)
    return render_template('/edit.html', recipe=recipe)

@app.route('/recipes/update/<int:id>', methods=['POST'])
def update(id):
    if not Recipe.validate_recipe(request.form):
        return redirect(f'/recipes/edit/{id}')
    data = {
        'name': request.form['name'],
        'description': request.form['description'],
        'under_30_minutes': request.form['under_30_minutes'],
        'instructions': request.form['instructions'],
        'date_made': request.form['date_made'],
        'id': id
    }
    Recipe.update(data)
    return redirect('/dashboard')

