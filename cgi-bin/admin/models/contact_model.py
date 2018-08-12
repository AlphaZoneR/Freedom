from models.database import *

class BaseContact(db.Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True)
    fname = Column(String(255), nullable=False)
    lname = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    subject = Column(String(255), nullable=False)
    body = Column(Text(8192), nullable=False)
    timestamp = Column(TIMESTAMP, nullable=False)

    def create():
        if not db.engine.dialect.has_table(db.engine, 'contacts'):
            BaseContact.__table__.create(db.engine)


    def __repr__(self):
        return json.dumps({
            'name': f'{self.fname} {self.lname}',
            'email': self.email,
            'subject': self.subject,
            'body': self.body,
            'timestamp': str(self.timestamp.strftime('%A %d %B %Y at %H:%M')),
            'id': self.id
        })

class Contact(BaseContact):
    
    def all():
        return db.session.query(Contact)

    
    def get(id):
        try:
            q = db.session.query(Contact).filter(Contact.id == id)
            return json.dumps({
                'status': 'OK',
                'code': 200,
                'contact': repr(q[0])
            })
        except Exception as error:
            print(repr(error))
            
            return json.dumps({
                'status': 'ERROR',
                'code': 500,
                'message': repr(error)
            })
    
    def add(data):
        try:
            contact = Contact(fname=data['fname'], lname=data['lname'], email=data['email'], 
                subject=data['subject'], body=data['body'], timestamp=datetime.now())
            db.session.add(contact)
            db.session.commit()

            return json.dumps({
                'status': 'OK',
                'code': 200
            })
        except Exception as error:
            print(repr(error))

            db.session.rollback()

            return json.dumps({
                'status': 'ERROR',
                'code': 500,
                'message': repr(error)
            })