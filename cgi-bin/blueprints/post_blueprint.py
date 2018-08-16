from flask import Response, Blueprint, abort, request, render_template, send_from_directory, session
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
        authors.append(json.loads(repr(User.get(id=post.author).all()[0])))
    return render_template('get_post.html', posts=[json.loads(repr(post)) for post in Post.all().order_by(Post.timestamp.desc()).all()], authors=authors)

@post_blueprint.route('/img/<img>', methods=['GET'])
def get_img(img):
    try:
        return send_from_directory('admin/img/posts/', img)
    except:
        return abort(404)

@post_blueprint.route('/get/<id>', methods=['GET'])
def get_by_id(id):
    try:
        post = Post.get(id=id)
        if 'posts_viewed' in session:
            if id not in session['posts_viewed']:
                post.update(views=post.views+1)
                session['posts_viewed'].append
        else:
            session['posts_viewed'] = []
            session['posts_viewed'].append(id)
            post.update(views=post.views+1)
        
        user = json.loads(repr(User.get(id=post.author).all()[0]))
        return render_template('post_id.html', post=post, user=user)
    except Exception as error:
        return message(503, repr(error))