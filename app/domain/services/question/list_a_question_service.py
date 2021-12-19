from typing import Tuple
from app.domain.ports.repository.repository_question import RepositoryQuestion


class ListAQuestionService:
    repository_question: RepositoryQuestion

    def __init__(self,
                 repository_question: RepositoryQuestion
                 ) -> None:
        self.repository_question = repository_question

    def execute(self, id: int) -> Tuple[dict, int]:
        response = self.repository_question.list_a_question(id=id)
        return str(response), 200
