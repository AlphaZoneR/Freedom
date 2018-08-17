from models.database import *

from utilities.login import *

import os, sys

class BaseUser(db.Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    creation = Column(TIMESTAMP, nullable=False)
    last_login = Column(TIMESTAMP)
    session = Column(String(255))
    picture = Column(String(255))

    def __repr__(self):
        return json.dumps({
            'email': self.email,
            'name': self.name,
            'picture': self.picture
        })
    def create():
        if not db.engine.dialect.has_table(db.engine, 'users'):
            BaseUser.__table__.create(db.engine)

class User(BaseUser):

    def count():
        try:
            count = db.session.query(User).count()
            db.session.commit()
            return count
        except Exception as error:
            db.session.rollback()
            return -1

    def all():
        return db.session.query(User)
    
    def get(**kwargs):
        try:
            result = User.all()
            for arg in kwargs:
                result = result.filter(getattr(User, arg) == kwargs[arg])
            return result
        except Exception as error:
            Utilities.write_to_log(error)
            return None
    
    def add(**kwargs):
        try:
            user = User(email=kwargs['email'], password=kwargs['password'], name=kwargs['name'], creation=datetime.now(), last_login=datetime.now(), picture='/img/users/default.png')
            user.save()
        except Exception as error:
            Utilities.write_to_log(error)


    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except Exception as error:
            Utilities.write_to_log(error)
            db.session.rollback()
            return error

    def update(self, **kwargs):
        try:
            User.all().filter(User.id == self.id).update(kwargs)
            db.session.commit()
            return self
        except Exception as error:
            Utilities.write_to_log(error)
            db.session.rollback()
            return self
