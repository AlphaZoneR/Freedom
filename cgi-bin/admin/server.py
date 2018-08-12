#!/home/freedom/Freedom/cgi-bin/venv/bin/python

import json
import os
import random
import string
from datetime import datetime, timedelta

from flask import (Flask, Response, abort, flash, redirect, render_template,
                   request, send_from_directory, session, url_for)
from gevent.pywsgi import WSGIServer
from PIL import Image

from blueprints.board_blueprint import board_blueprint
from blueprints.identity_blueprint import identity_blueprint
from blueprints.static_blueprint import static_blueprint
from blueprints.upload_blueprint import upload_blueprint
from blueprints.post_blueprint import post_blueprint
from models.board_model import Board
from models.contact_model import Contact
from models.user_model import User
from models.post_model import Post
from utilities.login import *

save_pid()

User.create()
Contact.create()
Board.create()
Post.create()


app = Flask(__name__)

N = 500
app.secret_key = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(N))

@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=60)

@app.route('/')
def index():
    if 'key' in session:
        if check_session():
            return render_template('panel.html', session=session, users=[json.loads(repr(contact)) for contact in Contact.all().order_by(Contact.id.desc()).all()])
    return render_template('login.html', failed=session.get('failed'))


@app.route('/contacts', methods=['POST'])
def contacts():
    if 'key' in session:
        if check_session():
            return render_template('contacts.html', users=[json.loads(repr(contact)) for contact in Contact.all().order_by(Contact.id.desc()).all()])
    else:
        return redirect('/login')


app.register_blueprint(identity_blueprint, url_prefix='/')
app.register_blueprint(static_blueprint, url_prefix='/')
app.register_blueprint(upload_blueprint, url_prefix='/')
app.register_blueprint(board_blueprint, url_prefix='/board')
app.register_blueprint(post_blueprint, url_prefix='/posts')


app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
# app.run('localhost', port=8080, debug=True)

http_server = WSGIServer(('localhost', 8080), app)
http_server.serve_forever()