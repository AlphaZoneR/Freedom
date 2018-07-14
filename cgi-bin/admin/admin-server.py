#!/home/afim1689/Freedom/cgi-bin/venv/bin/python

from flask import Response, Flask

from wsgiref.handlers import CGIHandler

app = Flask(__name__)

@app.route('/', methods=['GET'])
def root():
    return Response('ok')

CGIHandler().run(app)
