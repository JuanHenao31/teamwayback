from flask.json import jsonify
from flask import request

from app.database.repositories.question_repository import QuestionRepository
from app.domain.services.question.list_all_question_service import ListQuestionService


def list_all_question():

    question_repository = QuestionRepository()

    limit = request.args.get('limit', None)
    offset = request.args.get('offset', None)

    service = ListQuestionService(
        repository_question=question_repository)

    try:
        result, status_code = service.execute(limit=limit, offset=offset)
        return result, status_code
    except:
        return jsonify({'message': 'Internal server error'}), 500
