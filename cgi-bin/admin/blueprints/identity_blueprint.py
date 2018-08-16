import random
import string
from datetime import datetime
from hashlib import sha256

from flask import (Blueprint, Response, abort, redirect, render_template,
                   request, send_from_directory, session, url_for)

from models.user_model import User
from utilities.login import *

SALT = 'salt'

identity_blueprint = Blueprint('identity_blueprint', __name__)

@identity_blueprint.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.get(email=request.form['username'], password=sha256(f'{SALT}{request.form["password"]}'.encode()).hexdigest())
        if user != None and user.count() != 0:
            session['name'] = user[0].name
            session['email'] = user[0].email
            session['image'] = user[0].picture
            session['key'] = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(15))

            user[0].update(session=session['key'], last_login=datetime.now())
        else:
            session.clear()
            session['failed'] = True
    return redirect('/admin/#overall')

@identity_blueprint.route('/logout')
def logout():
    session.clear()
    return redirect('/admin/')
