from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 1
    return render_template('index.html')

@app.route('/2')
def add_2():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 1
    return redirect('/')   

@app.route('/specify', methods=['POST'])
def speficy():
    if 'count' in session:
        session['count'] += int(request.form['increment']) - 1
    else:
        session['count'] = 1
    return redirect('/')

@app.route('/destroy_session')
def reset():
    session.pop('count')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)