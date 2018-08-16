#!/home/freedom/Freedom/cgi-bin/venv/bin/python

from wsgiref.handlers import CGIHandler

import sys

from flask import Flask, Response, abort, request, session

from datetime import datetime, timedelta

from _thread import start_new_thread

from blueprints.contact_blueprint import contact_bp
from blueprints.board_blueprint import board_blueprint
from blueprints.post_blueprint import post_blueprint

from time import strftime

app = Flask(__name__)
app.secret_key = 'VGDd6TMyT3EmwkIA0xGfOVjOvAHb1RSfkAclRpvGou6DEYuvwWmTcAb7kfCA7WWgSA4auZlO3KrBENS7VKQB74CA3B4FdZ6GMuACv3O11MMq24eqBtilAvljJRI14CKDC6ZmO7nTMzCM9fJdDRxWeC4vLy1FOl9ppk4mx7H4eDoGTc8szZsMXN20Ux3pcmtF6GXGnnjHOqPnFhutqcNBLy19akpcVyTEezFO1U4Izc3XOEzD2KjLqeODEqN6nUS2TYhSgqPbZg8pB4lsw2LQS4rLXazx7Al8u7KFjLSGr57WcHBU4Xl8y18FRtm8UgyfLsgSmkWl3Btc2dJsSn0YBr5wmZqhqI05Ug8SUpRo329r2gardnYjVhRSfLBrL5knNU1MtefBy9IaJR5gyDkayzOEjTD9Wi0qOUHHgMC4wSyuoHT2pw1wMn0HgVOCjCjTM9obMgZP2iODfDNwdQF18or8rlBBeJyOPxUiGNd40bxq824Ny4Sa'
app.config['SESSION_TYPE'] = 'filesystem'

@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(days=31)

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
