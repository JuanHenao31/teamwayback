from flask.json import jsonify

from app.database.repositories.question_repository import QuestionRepository
from app.domain.services.question.list_a_question_service import ListAQuestionService


def list_a_question(id: int):
    question_repository = QuestionRepository()

    service = ListAQuestionService(
        repository_question=question_repository)

    try:
        result, status_code = service.execute(id=id)
        return result, status_code
    except:
        return jsonify({'message': 'Internal server error'}), 500
