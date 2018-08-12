from flask import Response, Blueprint, abort, request, render_template
from models.post_model import Post

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

    return render_template('get_post.html', posts=Post.all().all())