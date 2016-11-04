#!/usr/bin/python

from flask import Flask, jsonify, session
from flask import send_file, send_from_directory

context = ('../ssl/cert.pem', '../ssl/key.pem')

data = {
    'name': 'Artem',
    'command': 'Greatings',
}

app = Flask(__name__)


@app.route('/')
def root_html():
    return send_file('static/html/index.html')


@app.route('/js/<path:path>')
def root_js(path):
    return send_from_directory('static/js', path)


@app.route('/css/<path:path>')
def root_css(path):
    return send_from_directory('static/css', path)


@app.route('/counter')
def counter():
    session['username']['name'] = 'Polina'
    return jsonify(session['username'])

# for session we need to set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == '__main__':
    #app.run(debug=True, ssl_context=context)
    #app.run(ssl_context=context)
    app.run(debug=True)
