#!/usr/bin/python3 
from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return 'hello.'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
# http://127.0.0.1:5000/
# http://192.168.0.223:5000/
