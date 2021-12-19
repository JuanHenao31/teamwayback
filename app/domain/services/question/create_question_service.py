from typing import Tuple, Union

from app.domain.model.dto.question_dto import QuestionDto
from app.domain.ports.repository.repository_question import RepositoryQuestion


class CreateQuestionService:
    repository_question: RepositoryQuestion

    def __init__(self,
                 repository_question: RepositoryQuestion
                 ) -> None:
        self.repository_question = repository_question

    def execute(self, question_dto: QuestionDto) -> Tuple[dict, int]:

        response = self.repository_question.create(question_dto)

        return {'question': response}, 201
