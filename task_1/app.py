import hashlib
import sys

from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def post():
    print(request.form, file=sys.stdout)
    incoming = request.form['incoming_string'].encode('utf-8')
    incoming = hashlib.md5(incoming)
    return incoming.digest()


@app.route('/', methods=['GET'])
def info():
    return 'This here route returns MD5 hash of the string'


app.run()
