import json
import os
import random
import string
from datetime import datetime, timedelta

from flask import (Blueprint, Response, abort, flash, redirect,
                   render_template, request, send_from_directory, session,
                   url_for)
from PIL import Image

from models.board_model import Board
from utilities.login import *

board_blueprint = Blueprint('board_blueprint', __name__)

@board_blueprint.route('', methods=['POST'])
def board():
    try:
        if 'key' in session:
            if check_session():
                return render_template('board.html', board=[json.loads(repr(board)) for board in Board.all()])
            else:
                return redirect('/admin/login')
    except Exception as error:
        return message(503, repr(error))

@board_blueprint.route('/', methods=['POST'])
def board2():
    try:
        if 'key' in session:
            if check_session():
                return render_template('board.html', board=[json.loads(repr(board)) for board in Board.all()])
            else:
                return redirect('/admin/login')
    except Exception as error:
        return message(503, repr(error))

@board_blueprint.route('/update', methods=['POST'])
def update():
    try:
        if 'key' in session:
            if check_session():
                board = Board.get(name=request.form['old_name'])
                if board.picture == 'default.png':
                    board.update(name=request.form['name'], email=request.form['email'], phone=request.form['phone'], picture=request.form['image'].split('/')[-1], position=request.form['position'])
                elif board.picture != 'default.png' and request.form['image'].split('/')[-1] == 'default.png':
                    board.update(name=request.form['name'], email=request.form['email'], phone=request.form['phone'], position=request.form['position'])
                else:
                    board.update(name=request.form['name'], email=request.form['email'], phone=request.form['phone'], picture=request.form['image'].split('/')[-1], position=request.form['position'])
                return message(200, 'OK')
        else:
            return redirect('/admin/login')
    except Exception as error:
        return message(503, repr(error))

@board_blueprint.route('/add', methods=['POST'])
def add():
    try:
        if 'key' in session:
            if check_session():
                board = Board(name=request.form['name'], email=request.form['email'], phone=request.form['phone'], picture='default.png', position=request.form['position'])
                board.save()
                return message(200, 'OK')
        else:
            return redirect('/admin/login')
    except Exception as error:
        return message(503, repr(error))

@board_blueprint.route('/get', methods=['GET'])
def get():
    try:
        return render_template('get_board.html', board=[json.loads(repr(board)) for board in Board.all()])
    except Exception as error:
        return message(503, repr(error))


@board_blueprint.route('/remove', methods=['POST'])
def remove():
    try:
        if not check_session():
            return redirect('/admin/')

        board = Board.get(name=request.form['name'], email=request.form['email'])
        board.remove()

        return message(200, 'OK')

    except Exception as error:
        return message(503, repr(error))