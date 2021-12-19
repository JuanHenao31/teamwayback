from abc import abstractmethod
from typing import List

from app.domain.model.dto.result_dto import ResultDto
from app.domain.model.entity.result import Result


class RepositoryResult:

    @abstractmethod
    def create(self, result: Result) -> int:
        raise Exception('Not implemented method')

    @abstractmethod
    def update(self, result_id: int, result: Result):
        raise Exception('Not implemented method')

    @abstractmethod
    def delete(self, id: int):
        raise Exception('Not implemented method')

    @abstractmethod
    def list_a_result(self, value: int) -> List[ResultDto]:
        raise Exception('Not implemented method ')