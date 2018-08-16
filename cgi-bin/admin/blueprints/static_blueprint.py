from flask import (Blueprint, Response, abort, redirect, render_template,
                   request, send_from_directory, session, url_for)

from utilities.login import *

from blueprints.board_blueprint import Board
from blueprints.post_blueprint import Post

static_blueprint = Blueprint('static_blueprint', __name__)


@static_blueprint.route('/js/<path:path>')
def js_server(path):
    try:
        return send_from_directory('js', path)
    except Exception as error:
        print(error)
        abort(404)

@static_blueprint.route('/css/<path:path>')
def css_server(path):
    try:
        return send_from_directory('css', path)
    except Exception as error:
        print(error)
        return abort(404)

@static_blueprint.route('/webfonts/<path:path>')
def webfonts_css(path):
    try:
        return send_from_directory('webfonts', path)
    except Exception as error:
        print(error)
        return abort(404)


@static_blueprint.route('/img/<where>/<image>', methods=['GET'])
def images(where, image):
    try:
        return send_from_directory(f'img/{where}', image)
    except Exception as error:
        print(error)
        return abort(404)


@static_blueprint.route('/overall', methods=['POST'])
def overall():
    try:
        return render_template('overall.html', members=Board.count(), views=Post.get_views(), posts=Post.count())
    except Exception as error:
        return message(503, repr(error))