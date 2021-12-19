from typing import Tuple
from flask import request

from app.domain.model.dto.question_dto import QuestionDto
from app.modules.util.question_answer_util import save_new_question_util


def save_new_question() -> Tuple[dict, int]:

    data = request.get_json()

    question_data = QuestionDto(
        content=data['content']
    )

    return save_new_question_util(question_data)