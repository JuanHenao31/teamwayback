from dataclasses import dataclass


@dataclass
class AnswerDto:

    def __init__(self, content: str, weight: float, question_id: int) -> None:
        self.content = content
        self.weight = weight
        self.question_id = question_id

    def validate(self) -> None:
        required_fields = ['content', 'score', 'question_id']

        for field in required_fields:
            if not hasattr(self, field):
                raise 'Missing required field: %s' % field
