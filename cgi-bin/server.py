#!/home/freedom/Freedom/cgi-bin/venv/bin/python

from wsgiref.handlers import CGIHandler

import sys

from flask import Flask, Response, abort, request

from blueprints.contact_blueprint import contact_bp
from blueprints.board_blueprint import board_blueprint

from time import strftime

app = Flask(__name__)


# app.config['APPLICATION_ROOT'] = ''
app.register_blueprint(contact_bp, url_prefix='/contact')
app.register_blueprint(board_blueprint, url_prefix='/board')

@app.after_request
def after_request(resp):
	f = open('output', 'a')
	ts = strftime('[%Y-%b-%d %H:%M]')
	f.write(f'{ts} {request.remote_addr} {request.method} {request.scheme} {request.full_path} {resp.status}\n')
	f.close()

	return resp

CGIHandler().run(app)
