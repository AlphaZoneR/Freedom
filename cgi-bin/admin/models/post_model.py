from models.database import *

from utilities.login import *

class BasePost(db.Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    author = Column(Integer, ForeignKey('users.id'), nullable=False)
    title = Column(String(255), nullable=False)
    body = Column(Text(128000), nullable=False)
    timestamp = Column(TIMESTAMP, nullable=False)
    views = Column(Integer, nullable=False)
    picture = Column(String(255), nullable=True)

    def create():
        if not db.engine.dialect.has_table(db.engine, 'posts'):
            BasePost.__table__.create(db.engine)
    
    def __repr__(self):
        return json.dumps({
            'id': self.id,
            'title': self.title,
            'views': self.views,
            'body': self.body,
            'timestamp': str(self.timestamp.strftime('%A %d %B %Y at %H:%M')),
            'picture': self.picture
        })


class Post(BasePost):

    def count():
        try:
            count = db.session.query(Post).count()
            db.session.commit()
            return count
        except Exception as error:
            db.session.rollback()
            Utilities.write_to_log(error)
            return -1

    def get_views():
        try:
            posts = db.session.query(Post).all()
            summ = 0
            for post in posts:
                summ += post.views
            return summ 
        except Exception as error:
            Utilities.write_to_log(error)
            return -1

    def all():
        return db.session.query(Post)

    def get(**kwargs):
        try:
            db.session.expire_all()
            result = db.session.query(Post)
            for arg in kwargs:
                result = result.filter(getattr(Post, arg) == kwargs[arg])
            db.session.commit()
            return result.all()[0]
        except Exception as error:
            db.session.rollback()
            Utilities.write_to_log(error)
            return None
    
    def add(**kwargs):
        try:
            post = Post(author=kwargs['author'], title=kwargs['title'], body=kwargs['body'], timestamp=datetime.now(), picture=kwargs['picture'], views=1)
            post.save()
            return True
        except Exception as error:
            Utilities.write_to_log(error)
            return False
    
    def update(self, **kwargs):
        try:
            db.session.query(Post).filter(Post.id == self.id).update(kwargs)
            db.session.commit()
            return self
        except Exception as error:
            Utilities.write_to_log(error)
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
            Utilities.write_to_log(error)
            db.session.rollback()
