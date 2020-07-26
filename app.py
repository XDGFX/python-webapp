#!/usr/bin/env python3

from webapp import webserver
from webapp import websocket
import time

webserver.start_server()
time.sleep(2)
websocket.start_server()
