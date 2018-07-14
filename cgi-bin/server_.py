#!/xampp/cgi-bin/freedom/venv/Scripts/python

from wsgiref.handlers import CGIHandler

import sys

from flask import Flask, Response, abort, request

from blueprints.contact_blueprint import contact_bp

app = Flask(__name__)

# app.config['APPLICATION_ROOT'] = ''
app.register_blueprint(contact_bp, url_prefix='/contact')

CGIHandler().run(app)