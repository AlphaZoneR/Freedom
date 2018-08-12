#!/home/freedom/Freedom/cgi-bin/venv/bin/python

from wsgiref.handlers import CGIHandler

import sys

from flask import Flask, Response, abort, request

from _thread import start_new_thread

from blueprints.contact_blueprint import contact_bp
from blueprints.board_blueprint import board_blueprint
from blueprints.post_blueprint import post_blueprint

from time import strftime

app = Flask(__name__)

def write_log():
	f = open('output', 'a')
	ts = strftime('[%Y-%b-%d %H:%M]')
	f.write(f'{ts} {request.remote_addr} {request.method} {request.scheme} {request.full_path} {resp.status}\n')
	f.close()


# app.config['APPLICATION_ROOT'] = ''
app.register_blueprint(contact_bp, url_prefix='/contact')
app.register_blueprint(board_blueprint, url_prefix='/board')
app.register_blueprint(post_blueprint, url_prefix='/post')

@app.after_request
def after_request(resp):
	start_new_thread(write_log, ())
	return resp

CGIHandler().run(app)
