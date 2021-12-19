from typing import Tuple
from flask import request

from app.domain.model.dto.answer_dto import AnswerDto
from app.modules.util.question_answer_util import save_new_answer_util


def save_new_answer() -> Tuple[dict, int]:
    data = request.get_json()

    answer_data = AnswerDto(
        content=data['content'],
        weight=data['weight'],
        question_id=data['question_id']
    )

    return save_new_answer_util(answer_data)
