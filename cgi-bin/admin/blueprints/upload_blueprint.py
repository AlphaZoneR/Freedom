import json
import os
import random
import string

from flask import (Blueprint, Response, abort, redirect, render_template,
                   request, send_from_directory, session, url_for)
from PIL import Image

from utilities.login import *

upload_blueprint = Blueprint('upload_blueprint', __name__)

@upload_blueprint.route('/upload/board', methods=['POST'])
def upload_board():
    try:
        if 'key' in session:
            if check_session():
                if 'file' not in request.files:
                    return message(503, 'No file!')
                file = request.files['file']
                
                if file.filename == '':
                    return message(503, 'No file!')

                if file:
                    filename = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(50))
                    extension = file.filename.split('.')[1].lower()
                    filename += '.' + extension

                    if extension.lower() != 'jpg' and extension.lower() != 'png' and extension.lower() != 'bmp':
                        return message(503, 'Invalid format')

                    file.save(f'img/board/{filename}')
                    img = Image.open(f'img/board/{filename}')
                    img = img.resize((img.size[0], img.size[1]))
                    img.save(f'img/board/{filename}')
                    return Response(json.dumps({
                        'result': 200,
                        'filename': filename
                    }))

        return message(404, 'Unknown error!')
    except Exception as error:
        return message(503, repr(error))
@upload_blueprint.route('/upload/edit', methods=['POST'])
def upload_temp():
    try:
        if 'key' in session:
            if check_session():
                if 'file' not in request.files:
                    return message(503, 'No file')

                file = request.files['file']
                
                if file.filename == '':
                    return message(503, 'No file')

                if file:
                    filename = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(50))
                    extension = file.filename.split('.')[1].lower()
                    filename += '.' + extension
                    file.save(f'img/temp/{filename}')
                    img = Image.open(f'img/temp/{filename}')
                    img = img.resize((img.size[0], img.size[1]))
                    img.save(f'img/temp/{filename}')
                    return Response(json.dumps({
                        'result': 200,
                        'filename': filename
                    }))

        return message(503, 'Unknown error')
    except Exception as error:
        return message(503, repr(error))


@upload_blueprint.route('/upload/move', methods=['POST'])
def copy_temp():
    if not check_session():
        return redirect('/admin/')
    try:
        data = json.loads(request.form['files'])

        for img in data:
            os.rename(f'img/temp/{img}', f'img/posts/{img}')
        
        return message(200, 'OK')
    except Exception as error:
        return message(503, repr(error))
