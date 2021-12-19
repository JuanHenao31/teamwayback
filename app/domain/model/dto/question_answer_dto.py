from dataclasses import dataclass

from app.domain.model.dto.answer_dto import AnswerDto


@dataclass
class QuestionAnswerDto:

    def __init__(self, content: str, answers_dto: list[AnswerDto]) -> None:
        self.content = content
        self.answers_dto = answers_dto

    def validate(self) -> None:
        required_fields = ['content', 'answers_dto']

        for field in required_fields:
            if not hasattr(self, field):
                raise 'Missing required field: %s' % field
