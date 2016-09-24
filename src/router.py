#!/usr/bin/python
from flask import Flask, jsonify, session

data = {
    'name': 'Artem',
    'command': 'Greatings',
}

app = Flask(__name__)

@app.route('/')
def index():
    session['username'] = data
    return jsonify(data)

@app.route('/counter')
def counter():
    session['username']['name'] = 'Polina'
    return jsonify(session['username'])

# for session we need to set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == '__main__':
    app.run(debug=True)
