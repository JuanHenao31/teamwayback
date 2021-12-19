from abc import abstractmethod

from app.domain.model.entity.answer import Answer


class RepositoryAnswer:

    @abstractmethod
    def create(self, answer: Answer) -> int:
        raise Exception('Not implemented method')

    @abstractmethod
    def update(self, answer_id: int, answer: Answer):
        raise Exception('Not implemented method')

    @abstractmethod
    def delete(self, id: int):
        raise Exception('Not implemented method')
