from . import app, db
from .config import Config
from .models import Question
from .external_requests import get_questions_from_jservice

from typing import Tuple, Set
from flask import request, jsonify, Response
from sqlalchemy.exc import IntegrityError
from sqlalchemy import inspect
from requests import ConnectionError

@app.route('/add_question', methods=['POST', 'GET'])
def post_questions() -> Tuple[Response, int]:
    prev_question: Question
    prev_question = Question.query.order_by(Question.id.desc()).limit(1).first()

    if request.method == 'GET':
        return jsonify(result='Bad request. Use POST'), 400

    elif request.method == 'POST':
        content: Response
        questions: Set[Question]
        questions_num: int

        content = request.get_json()
        questions_num = content['questions_num']

        try:
            questions = get_questions_from_jservice(questions_num)

            not_added_questions: int = questions_num
            iter_counter: int = 0 # count itteration to not get infinite while

            while not_added_questions > 0:
                if iter_counter > Config.MAX_WHILE_REQUESTS_DEPTH:
                    raise RecursionError

                for question in questions:
                    try:
                        db.session.add(question)
                        db.session.commit()
                    except IntegrityError:
                        db.session.rollback()
                    else:
                        not_added_questions -= 1
                if not_added_questions > 0:
                    iter_counter += 1
                    questions = get_questions_from_jservice(not_added_questions) # get list of missing questions

        except ValueError as err:
            return jsonify(result=f'Bad request: {str(err)}'), 400
        except ConnectionError as err:
            return jsonify(result=f'Internal Server Error: API Connection troubles'), 500
        except RecursionError as err:
            return jsonify(result=f'Internal Server Error: Can\'t get unique questions, try again later'), 500
        else:
            if not prev_question:
                return Response('{}'), 201
            else:
                return jsonify({c.key: getattr(prev_question, c.key)
                                for c in inspect(prev_question).mapper.column_attrs}), 201
