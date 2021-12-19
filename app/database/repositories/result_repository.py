from typing import List, Optional

from sqlalchemy import and_

from app.database.config.db_connection import DBConnection
from app.database.tables.result import ResultModel
from app.domain.model.dto.result_dto import ResultDto
from app.domain.model.entity.result import Result
from app.domain.ports.repository.repository_result import RepositoryResult


class ResultRepository(RepositoryResult):

    def list_a_result(self, value: int) -> Optional[ResultDto]:
        with DBConnection() as connection:
            try:
                result = connection.session.query(
                    ResultModel).filter(
                    ResultModel.min_value <= value, ResultModel.max_value >= value
                ).first()
                if result is not None:
                    print("Hi")
                    new_result = result.to_core_model()
                    return ResultDto(id=new_result.id, content=new_result.content,
                                     min_value=new_result.min_value,
                                     max_value=new_result.max_value)
                return None
            except:
                return None
            finally:
                connection.session.close()

    def create(self, result: Result) -> int:
        pass

    def update(self, result_id: int, result: Result):
        pass

    def delete(self, id: int):
        pass
