from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database.config.db_base import Base
from app.domain.model.entity.question import Question


class QuestionModel(Base, Question):
    __tablename__ = "question"

    id = Column('id', Integer, primary_key=True,
                autoincrement=True)

    content = Column(String(300))

    answers = relationship('AnswerModel', backref='question')

    def __repr__(self) -> str:
        return ' "Question ": [{ "id":%d, "content" : %s }]' % (self.id, self.content)

    def to_core_model(self) -> Question:
        return Question(
            id=self.id,
            content=self.content
        )