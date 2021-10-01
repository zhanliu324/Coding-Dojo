from flask_app import app
from flask import render_template, redirect, request
from flask_app.models import dojo, ninja

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    return render_template('dojos.html', dojos = dojo.Dojo.get_all())

@app.route('/dojos/create', methods=['POST'])
def create_dojo():
    dojo.Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/dojos/<int:dojo_id>')
def dojo_show(dojo_id):
    data = {'id': dojo_id}
    dojo_with_ninjas = dojo.Dojo.get_dojo_with_ninjas(data)
    return render_template('/dojo_show.html', dojo = dojo_with_ninjas)