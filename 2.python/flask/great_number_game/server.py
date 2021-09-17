from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "secret"

@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 0
    if 'number' not in session:
        session['number'] = 50
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    session['guess'] = int(request.form['guess'])
    session['count'] += 1
    return redirect('/')

@app.route('/reset')
def reset():
    session.pop('number')
    session.pop('guess')
    session.pop('count')
    # session.pop('winners')
    return redirect('/')

@app.route('/register', methods=['POST'])
def register():
    if 'winners' not in session:
        session['winners'] = []
    winners = session['winners']
    winner = {'name': request.form['name'], 'attempts': int(session['count'])}
    winners.append(winner)
    print(winners)
    session['winners'] = winners
    return redirect('/leaderboard')


@app.route('/leaderboard')
def leaderboard():
    print(session['winners'])
    return render_template('leaderboard.html', winners = session['winners'])

if __name__ == '__main__':
    app.run(debug=True)