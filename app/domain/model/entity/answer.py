from dataclasses import dataclass


@dataclass
class Answer:
    def __init__(self,
                 content: str,
                 weight: float,
                 question_id: int,
                 id: int = None) -> None:
        self.id = id
        self.content = content
        self.weight = weight
        self.question_id = question_id

    def __repr__(self) -> str:
        return '<Answer %r>' % self.content
