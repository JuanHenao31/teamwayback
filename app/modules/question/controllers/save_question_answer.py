from typing import Tuple
from flask import request

from app.domain.model.dto.answer_dto import AnswerDto
from app.domain.model.dto.question_dto import QuestionDto
from app.modules.util.question_answer_util import save_new_question_util, save_new_answer_util


def save_new_question_answer() -> Tuple[dict, int]:
    data = request.get_json()

    question_data = QuestionDto(
        content=data['content']
    )

    res, code = save_new_question_util(question_data)

    question_added_id = [int(s) for s in res.data.split() if s.isdigit()]

    answer_data = [AnswerDto(content=a['content'], weight=a['weight'], question_id=question_added_id[0]) for a in
                   data['answers_dto']]

    answer, code = [save_new_answer_util(b) for b in answer_data]

    return res
