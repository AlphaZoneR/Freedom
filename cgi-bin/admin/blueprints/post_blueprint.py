import json
import os
import random
import string
from datetime import datetime, timedelta

from flask import (Blueprint, Response, abort, flash, redirect,
                   render_template, request, send_from_directory, session,
                   url_for)
from PIL import Image

from models.user_model import User
from models.post_model import Post
from utilities.login import *

from models.database import *

post_blueprint = Blueprint('post_blueprint', __name__)

@post_blueprint.before_request
def before_request():
    db.session.expire_all()

@post_blueprint.route('/', methods=['POST'])
def index():
    try:
        if check_session():
            return render_template('posts.html', posts=[json.loads(repr(post)) for post in Post.all()])
        else:
            return redirect('/')
    except Exception as error:
        return message(503, repr(error))


@post_blueprint.route('/add', methods=['POST', 'GET'])
def add():
    if not check_session():
        return redirect('/')
    
    if request.method == 'POST':
        try:
            user = User.get(name=session['name'], email=session['email']).limit(1).all()[0]
            post = Post(author=user.id, title=request.form['title'], body=request.form['body'], picture=request.form['picture'], views=0)
            post.save()
            return message(200, post.id)
        
        except Exception as error:
            return message(503, repr(error))
    elif request.method == 'GET':
        try:
            
            return render_template('add_post.html', user={'name': session['name']})
        except Exception as error:
            return message(503, repr(error))

@post_blueprint.route('/edit/<id>', methods=['GET', 'POST'])
def get(id):
    if not check_session():
        return redirect('/admin/')
    
    if request.method == 'GET':
        try:
            post = Post.get(id=id)
            
            if not post:
                return redirect('/admin/#posts')

            user = User.get(id=post.author).limit(1).all()[0]

            return render_template('post.html', post=json.loads(repr(post)), user=json.loads(repr(user)))
        except Exception as error:
            return message(503, repr(error))
    elif request.method =='POST':
        try:
            post = Post.get(id=id)

            if post:
                post.update(title=request.form['title'], timestamp=datetime.now(), body=request.form['body'])
                return message(200, 'OK')

            return message(503, 'Unknown error!')
        except Exception as error:
            return message(503, repr(error))

@post_blueprint.route('/remove', methods=['POST'])
def remove():
    if not check_session():
        return redirect('/admin/')

    try:
        post = Post.get(id=request.form['id'])
        post.remove()
        return message(200, 'OK')
    except Exception as error:
        return message(503, repr(error))
        