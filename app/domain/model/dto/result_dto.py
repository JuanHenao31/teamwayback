from dataclasses import dataclass


@dataclass
class ResultDto:

    def __init__(self,
                 min_value: int, max_value: int, content: str = None, id: int = None) -> None:
        self.id = id
        self.content = content
        self.min_value = min_value
        self.max_value = max_value

    def validate(self) -> None:
        required_fields = ['min_value', 'max_value']

        for field in required_fields:
            if not hasattr(self, field):
                raise 'Missing required field: %s' % field

    def __repr__(self) -> str:
        return 'Result : %d with Content :  %r ' % (self.id, self.content)
