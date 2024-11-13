#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return 'hello.'
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=4000)
# http://127.0.0.1:4000/