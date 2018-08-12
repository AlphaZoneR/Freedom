import os

from flask import Response, Blueprint, abort, request, render_template, send_from_directory
from models.board_model import Board

import json

def message(code, msg):
    print(msg)
    return json.dumps({
        'result': code,
        'message': msg
    })

board_blueprint = Blueprint('board_blueprint', __name__)

@board_blueprint.route('/get', methods=['GET'])
def get():
    try:
        return render_template('get_board.html', board=[json.loads(repr(board)) for board in Board.all()])
    except Exception as error:
        return abort(404)

@board_blueprint.route('/img/<image>', methods=['GET'])
def images(image):
    try:
        return send_from_directory(f'admin/img/board/', image)
    except Exception as error:
        return abort(404)