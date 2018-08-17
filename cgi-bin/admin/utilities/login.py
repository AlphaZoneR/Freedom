import json
from datetime import datetime

from flask import session

import sys, os

class Utilities:
    def write_to_log(error):
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        f = open('log/log.txt', 'a')
        f.write(f'[{str(datetime.now())}] {repr(error)}\n in {fname} on line {exc_tb.tb_lineno}')
        f.close()

def check_session():
    return 'key' in session

def write_to_log(error):
    f = open('log/log.txt', 'a')
    f.write(f'[{str(datetime.now())}] {repr(error)}\n')
    f.close()

def message(code, msg):
    return json.dumps({
        'result': code,
        'message': msg
    })

def save_pid():
    f = open('pid', 'w')
    f.write(str(os.getpid()))
    f.close()