import json
from datetime import datetime
from time import time

import pymysql
from sqlalchemy import (Column, ForeignKey, Integer, MetaData, String, Table,
                        Text, create_engine, insert, select, text, update)
from sqlalchemy.dialects.mysql import TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapper, scoped_session, sessionmaker


class Database:
    def __init__(self):
        self.m = MetaData()
        self.engine = create_engine('mysql+pymysql://freedom:freedom123@localhost/freedom')
        Session = scoped_session(sessionmaker(bind=self.engine, twophase=True))
        self.session = Session()
        self.Base = declarative_base()

db = Database()
