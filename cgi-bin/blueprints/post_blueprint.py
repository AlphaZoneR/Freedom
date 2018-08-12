from flask import Response, Blueprint, abort, request, render_template, send_from_directory
from models.post_model import Post
from models.user_model import User

import json


def message(code, msg):
    print(msg)
    return json.dumps({
        'result': code,
        'message': msg
    })

post_blueprint = Blueprint('post_blueprint', __name__)

@post_blueprint.route('/get', methods=['GET'])
def get_all():
    authors = []
    for post in Post.all().all():
        authors.append(User.get(id=post.author))
    return render_template('get_post.html', posts=[json.loads(repr(post)) for post in Post.all().all()], authors=authors)

@post_blueprint.route('/img/<img>', methods=['GET'])
def get_img(img):
    try:
        return send_from_directory('admin/img/posts/', img)
    except:
        return abort(404)