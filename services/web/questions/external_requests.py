from requests import get as requests_get, ConnectionError
from typing import Set

from .models import Question
from .config import Config


def get_questions_from_jservice(amount: int = 1) -> Set[Question]:
    result: Set[Question]
    question_text: str
    question_answer: str

    result = set()

    if amount > Config.MAX_JSERVICE_REQUESTS:
        raise ValueError(f"Too many requests. Must be less then {Config.MAX_JSERVICE_REQUESTS}") # If you want to increase it override MAX_JSERVICE_REQUESTS it in config.py

    if amount <= 0:
        raise ValueError("Wrong value. Must be more than 0")


    try:
        jservice_request = requests_get(f'https://jservice.io/api/random?count={amount}').json()

        for request_unit in jservice_request:
            question_text = request_unit.get('question')
            question_answer = request_unit.get('answer')
            question_created_at = request_unit.get('created_at')
            question_airdate = request_unit.get('airdate')
            jservice_id = request_unit.get('id')

            question = Question(question_text=question_text, question_answer=question_answer,
                                jservice_id=jservice_id, question_airdate=question_airdate,
                                question_created_at=question_created_at)
            result.add(question)

    except ConnectionError as err:
        raise err

    # It is unlikely that there will be too many identical questions, but then just throw out exception
    try:
        if len(result) < amount:
            result.union(get_questions_from_jservice(len(result) - amount))
    except RecursionError as err:
        raise err
    else:
        return result


