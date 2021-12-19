from flask import request
from flask.json import jsonify

from app.database.repositories.result_repository import ResultRepository
from app.domain.services.result.list_a_result_service import ListAResultService


def list_a_result():

    data = request.get_json()

    value = data["value"]

    result_repository = ResultRepository()

    service = ListAResultService(
        result_repository=result_repository)

    try:
        result, status_code = service.execute(value=value)
        return result, status_code
    except:
        return jsonify({'message': 'Internal server error'}), 500
