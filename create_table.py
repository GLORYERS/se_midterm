from sqlalchemy import *
from datetime import datetime

engine = create_engine('sqlite:///db.db')

metadata = MetaData()

chat1 = Table('chat1', metadata,
              Column('name', Text, primary_key=True,
                     nullable=False, unique=True),
              Column('message', Text, nullable=False),
              Column('time', DateTime, nullable=False)
              )

user = Table('user', metadata,
             Column('username', Text, primary_key=True,
                    nullable=False, unique=True),
             Column('password', Text, nullable=False)
             )

metadata.create_all(engine)
# class chat1(db.Model):
#     name = db.Column(db.Text, primary_key=True, nullable=False, unique=True)
#     message = db.Column(db.Text, nullable=False)
#     time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

#     def __repr__(self):
#         return 'name:{}, message:{}, time:{}'.format(
#             self.name,
#             self.message,
#             self.time
#         )


# class user(db.Model):
#     name = db.Column(db.Text, primary_key=True, nullable=False, unique=True)
#     pwd = db.Column(db.Text, nullable=False)
