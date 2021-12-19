from typing import Tuple

from app.domain.model.dto.result_dto import ResultDto
from app.domain.ports.repository.repository_result import RepositoryResult


class ListAResultService:
    result_repository: RepositoryResult

    def __init__(self,
                 result_repository: RepositoryResult
                 ) -> None:
        self.result_repository = result_repository

    def execute(self, value: int) -> Tuple[dict, int]:
        response = self.result_repository.list_a_result(value=value)
        return str(response), 200
