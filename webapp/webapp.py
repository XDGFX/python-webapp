#!/usr/bin/env python3
from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
from threading import Thread

app = Flask(__name__)

socketio = SocketIO(app, async_mode='threading')

# --- INITIALISATION ---
def serve():
    socketio.run(app)

def start_server():
    thread = Thread(target=serve)
    thread.start()
    print("Webserver started")

# --- SEND COMMANDS ---
def send(event, data):
    socketio.emit(str(event), {'data': data})

# --- WEBSERVER ROUTES ---
@app.route('/')
def index():
    return render_template('index.html')

# --- WEBSOCKET ROUTES ---
@socketio.on('my event')
def test_message(message):
    emit('my response', {'data': 'got it!'})