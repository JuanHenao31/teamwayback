from sqlalchemy import Column, Integer, String

from app.database.config.db_base import Base
from app.domain.model.entity.result import Result


class ResultModel(Base, Result):
    __tablename__ = "result"

    id = Column('id', Integer, primary_key=True,
                autoincrement=True)

    content = Column(String(300))

    min_value = Column(Integer)

    max_value = Column(Integer)

    def __repr__(self) -> str:
        return ' "Result ": [{ "id":%d, "content" : %s , "min_value" : %d , "max_value" : %d}]' \
               % (self.id, self.content, self.min_value, self.max_value)

    def to_core_model(self) -> Result:
        return Result(
            id=self.id,
            content=self.content,
            min_value=self.min_value,
            max_value=self.max_value
        )
