#!/usr/bin/env python3

from webapp import webapp

webapp.start_server()
# from webapp import webserver
# from webapp import websocket
# import time

webapp.send('my response', input("Input: "))

# webserver.start_server()
# time.sleep(2)
# websocket.start_server()
