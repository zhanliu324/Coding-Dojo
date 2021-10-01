from flask_app import app
from flask import render_template, redirect, request
from flask_app.models import dojo, ninja

@app.route('/ninjas')
def ninjas():
    return render_template('add_ninja.html', dojos = dojo.Dojo.get_all())

@app.route('/ninjas/create', methods = ['POST'])
def create_ninja():
    ninja.Ninja.save(request.form)
    return redirect(f"/dojos/{request.form['dojo_id']}")