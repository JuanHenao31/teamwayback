from dataclasses import dataclass


@dataclass
class Result:
    def __init__(self,
                 content: str,
                 min_value: int, max_value: int, id: int = None) -> None:
        self.id = id
        self.content = content
        self.min_value = min_value
        self.max_value = max_value

    def __repr__(self) -> str:
        return 'Your Result is  %r ' % self.content
