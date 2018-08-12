import json
from datetime import datetime

from flask import session

from models.user_model import User

import os

def check_session():
    return 'key' in session


def message(code, msg):
    print(msg)
    return json.dumps({
        'result': code,
        'message': msg
    })

def save_pid():
    f = open('pid', 'w')
    f.write(str(os.getpid()))
    f.close()