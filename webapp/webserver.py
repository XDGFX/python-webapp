#!/usr/bin/env python3

from flask import Flask, render_template
from threading import Thread

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


def serve():
    app.run(debug=False, host='localhost', port=9000)


def start_server():
    webserver_thread = Thread(target=serve)
    webserver_thread.start()
