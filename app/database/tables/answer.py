from sqlalchemy import Column, Integer, String, ForeignKey

from app.database.config.db_base import Base
from app.domain.model.entity.answer import Answer


class AnswerModel(Base, Answer):
    __tablename__ = "answer"

    id = Column('ID', Integer, primary_key=True,
                autoincrement=True)

    content = Column(String(300))

    weight = Column(Integer)

    question_id = Column(Integer, ForeignKey('question.id'))

    def __repr__(self) -> str:
        return '<AnswerModel id=%d, content=%s>' % (self.id, self.content)

    def to_core_model(self) -> Answer:
        return Answer(
            id=self.id,
            content=self.content,
            weight=self.weight,
            question_id=self.question_id
        )