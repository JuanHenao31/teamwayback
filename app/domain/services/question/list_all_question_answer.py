from typing import Tuple

from app.domain.ports.repository.repository_question import RepositoryQuestion


class ListQuestionAnswerService:
    repository_question: RepositoryQuestion

    def __init__(self,
                 repository_question: RepositoryQuestion,
                 ) -> None:
        self.repository_question = repository_question

    def execute(self, limit=0, offset=0) -> Tuple[dict, int]:
        response = self.repository_question.list_all_question_answer(limit=limit, offset=offset)
        return {'questions': response}, 200
