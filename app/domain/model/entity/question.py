from dataclasses import dataclass


@dataclass
class Question:
    def __init__(self,
                 content: str,
                 id: int = None) -> None:
        self.id = id
        self.content = content

    def __repr__(self) -> str:
        return 'Question : %d with Content :  %r added' % (self.id , self.content)
