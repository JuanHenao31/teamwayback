from abc import abstractmethod
from typing import List

from app.domain.model.dto.question_dto import QuestionDto
from app.domain.model.entity.question import Question


class RepositoryQuestion:

    @abstractmethod
    def create(self, question: Question) -> int:
        raise Exception('Not implemented method')

    @abstractmethod
    def update(self, question_id: int, question: Question):
        raise Exception('Not implemented method')

    @abstractmethod
    def delete(self, id: int):
        raise Exception('Not implemented method')

    @abstractmethod
    def list_all_question(self, limit=None, offset=None) -> List[QuestionDto]:
        raise Exception('Not implemented method ')

    @abstractmethod
    def list_a_question(self, id: int) -> List[QuestionDto]:
        raise Exception('Not implemented method ')
