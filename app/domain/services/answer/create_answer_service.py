from typing import Tuple, Union

from app.domain.model.dto.answer_dto import AnswerDto
from app.domain.ports.repository.repository_answer import RepositoryAnswer


class CreateAnswerService:
    repository_answer: RepositoryAnswer

    def __init__(self,
                 repository_answer: RepositoryAnswer
                 ) -> None:
        self.repository_answer = repository_answer

    def execute(self, answer_dto: AnswerDto) -> Tuple[dict, int]:
        response = self.repository_answer.create(answer_dto)
        return {'answer': response}, 201
