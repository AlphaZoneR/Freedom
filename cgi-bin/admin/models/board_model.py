if __name__ == '__main__':
    from database import *
else:
    from models.database import *

class BaseBoard(db.Base):
    __tablename__ = 'board'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(255), nullable=False, unique=True)
    email = Column(String(255), nullable=False)
    phone = Column(String(255), nullable=False)
    position = Column(String(255), nullable=False)
    picture = Column(String(255), nullable=False)

    def __repr__(self):
        return json.dumps({
            'email': self.email,
            'name': self.name,
            'picture': self.picture,
            'phone': self.phone,
            'position': self.position
        })
    def create():
        if not db.engine.dialect.has_table(db.engine, 'board'):
            BaseBoard.__table__.create(db.engine)


class Board(BaseBoard):

    def count():
        try:
            count = db.session.query(Board).count()
            db.session.commit()
            return count
        except Exception as error:
            db.session.rollback()
            return -1


    def all():
        try:
            return db.session.query(Board).all()
        except Exception as error:
            print(error)
            return False
    
    def get(**kwargs):
        try:
            result = db.session.query(Board)
            for arg in kwargs:
                result = result.filter(getattr(Board, arg) == kwargs[arg])
            db.session.commit()
            return result.all()[0]
        except Exception as error:
            db.session.rollback()
            print(repr(error))
            return None
    

    def add(**kwargs):
        try:
            board = Board(name=kwargs['name'], phone=kwargs['phone'], email=kwargs['email'], picture=kwargs['picture'])
            board.save()
            return True
        except Exception as error:
            print(error)
            return False
    
    def update(self, **kwargs):
        try:
            db.session.query(Board).filter(Board.id == self.id).update(kwargs)
            db.session.commit()
            return self
        except Exception as error:
            print(error)
            db.session.rollback()
            return self

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as error:
            print(repr(error))
            db.session.rollback()
    
    def remove(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception as error:
            print(error)
            db.session.rollback()

if __name__ == '__main__':
    Board.create()
    print(Board.get(id=1))
