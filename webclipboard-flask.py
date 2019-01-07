from flask import Flask, render_template, request
app = Flask(__name__)

clipboard = 'INITIAL VALUE TEST'

@app.route('/')
def load_clipboard():
    return render_template('form.html', clipboard=clipboard)

@app.route('/', methods=['POST'])
def save_clipboard():
    global clipboard
    clipboard = request.form['clipboard']
    return load_clipboard()
