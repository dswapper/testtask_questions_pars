from . import db


class BaseModel(db.Model):
    __abstract__ = True

    id =  db.Column(db.Integer(), primary_key = True)

    def __repr__(self):
        return "<{}:{}>".format(self.id, self.name)

class Question(BaseModel):
    __tablename__ = 'questions'

    jservice_id = db.Column(db.Integer(), unique=True, index=True)
    question_text = db.Column(db.String(511))
    question_answer = db.Column(db.String(511))
    question_created_at = db.Column(db.DateTime())
    question_airdate = db.Column(db.DateTime())
