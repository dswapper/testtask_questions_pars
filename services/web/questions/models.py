from . import db
from datetime import datetime


class BaseModel(db.Model):
    __abstract__ = True

    id =  db.Column(db.Integer(), primary_key = True)
    created_on = db.Column(db.DateTime(), default=datetime.utcnow())

    def __repr__(self):
        return "<{}:{}>".format(self.id, self.name)

class question(BaseModel):
    __tablename__ = 'questions'

    question_text = db.Column(db.String(511), unique=True)
    question_answer = db.Column(db.String(511))
