import json
from datetime import datetime
from time import time

import pymysql
from sqlalchemy import (Column, Integer, MetaData, String, Table,
                        create_engine, insert, select, text, update, Text)
from sqlalchemy.dialects.mysql import TIMESTAMP
from sqlalchemy.orm import mapper, sessionmaker

from sqlalchemy.ext.declarative import declarative_base

class Database:
    def __init__(self):
        self.m = MetaData()
        self.engine = create_engine('mysql+pymysql://username:password@localhost/freedom')
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        self.Base = declarative_base()

db = Database()
