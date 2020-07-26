#!/usr/bin/env python3

from webapp import webapp

webapp.start_server()

webapp.send('my response', input("Input: "))