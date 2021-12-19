from dataclasses import dataclass


@dataclass
class QuestionDto:

    def __init__(self, content: str  ,               id: int = None) -> None:
        self.id = id
        self.content = content

    def validate(self) -> None:
        required_fields = ['content']

        for field in required_fields:
            if not hasattr(self, field):
                raise 'Missing required field: %s' % field

    def __repr__(self) -> str:
        return 'Question : %d with Content :  %r ' % (self.id, self.content)
