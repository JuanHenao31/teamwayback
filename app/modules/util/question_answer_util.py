from flask import jsonify

from app.database.repositories.answer_repository import AnswerRepository
from app.database.repositories.question_repository import QuestionRepository
from app.domain.services.answer.create_answer_service import CreateAnswerService
from app.domain.services.question.create_question_service import CreateQuestionService


def save_new_question_util(question_data=None):
    question_repository = QuestionRepository()

    service = CreateQuestionService(
        repository_question=question_repository)

    try:
        result, status_code = service.execute(question_dto=question_data)
        return jsonify(result), status_code
    except:
        return jsonify({'message': 'Internal server error'}), 500


def save_new_answer_util(answer_data=None):
    answer_repository = AnswerRepository()

    service = CreateAnswerService(
        repository_answer=answer_repository)

    try:
        result, status_code = service.execute(answer_dto=answer_data)
        return jsonify(result), status_code
    except:
        return jsonify({'message': 'Internal server error'}), 500
