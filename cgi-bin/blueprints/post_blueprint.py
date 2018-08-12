from flask import Response, Blueprint, abort, request
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
    return Response(Post.all())