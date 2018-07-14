from flask import Response, Blueprint, abort, request
from models.contact_model import Contact

import json

import re
EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

Contact.create()

contact_bp = Blueprint('contact_bp', __name__)

@contact_bp.route('/get', methods=['POST'])
def contact_get():
    try:
        return Contact.get(request.form['id'])
    except Exception as error:
        return Response(repr(error))

@contact_bp.route('/get', methods=['GET'])
def contact_get_refuse():    
    abort(404)

@contact_bp.route('/add', methods=['POST'])
def contact_add():
    try:
        
        if request.form['fname'] == '' or request.form['fname'] == '' or request.form['subject'] == '' or re.match(EMAIL_REGEX, request.form['email']) == None or request.form['body'] == '':
            raise Exception('Invalid input data')
        
        return Contact.add({
            'fname': request.form['fname'],
            'lname': request.form['lname'],
            'email': request.form['email'],
            'subject': request.form['subject'],
            'body': request.form['body'],
        })
    except Exception as exception:
        return Response(json.dumps({
            'status': str(exception)
        }))

@contact_bp.route('/add', methods=['GET'])
def contact_add_refuse():    
    abort(404)