from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def form():
    session.clear()
    return render_template('form.html')

@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['gender'] = request.form['gender']
    session['location'] = request.form['location']
    session['comment'] = request.form['comment']
    languages = []
    for language in ['language1', 'language2', 'language3', 'language4']:
        if language in request.form:
            languages.append(request.form[language])
    session['languages'] = ', '.join(languages)
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)