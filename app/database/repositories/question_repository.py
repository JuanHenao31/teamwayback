from app.database.config.db_connection import DBConnection
from typing import List, Optional
from app.database.tables.question import QuestionModel
from app.domain.model.dto.question_answer_dto import QuestionAnswerDto
from app.domain.model.dto.question_dto import QuestionDto
from app.domain.model.entity.question import Question
from app.domain.ports.repository.repository_question import RepositoryQuestion


class QuestionRepository(RepositoryQuestion):

    def list_a_question(self, id: int) -> Optional[QuestionDto]:
        with DBConnection() as connection:
            try:
                question = connection.session.query(
                    QuestionModel).filter_by(id=id).first()
                if question is not None:
                    new_question = question.to_core_model()
                    return QuestionDto(id=new_question.id, content= new_question.content)
                return None

            except:
                return None
            finally:
                connection.session.close()

    def list_all_question(self, limit=None, offset=None) -> List[QuestionDto]:
        with DBConnection() as connection:
            try:
                return connection.session.query(QuestionModel).limit(limit=limit).offset(offset=offset).all()
            except:
                return []
            finally:
                connection.session.close()

    def create(self, question: Question) -> Question:
        question_params: Question = None

        if isinstance(question, QuestionAnswerDto):
            question_params = Question(
                content=question.content)
        else:
            question_params = question

        with DBConnection() as connection:
            try:
                question_to_save = QuestionModel(
                    content=question_params.content
                )

                connection.session.add(question_to_save)
                connection.session.commit()
                connection.session.flush()

                return question_to_save.to_core_model().__repr__()

            except:
                connection.session.rollback()
                raise Exception('Error on save Question')
            finally:
                connection.session.close()

    def update(self, question_id: int, question: Question) -> Question:
        with DBConnection() as connection:
            try:
                question_in_database = connection.session.query(
                    QuestionModel).filter_by(id=question_id).first()

                question_in_database.content = question.content
                question_in_database.answer = question.answer

                connection.session.commit()
                return question_in_database.to_core_model()
            except:
                return None
            finally:
                connection.session.close()

    def delete(self, id: int):
        with DBConnection() as connection:
            try:
                question_in_database = connection.session.query(
                    QuestionModel).filter_by(id=id).delete()
                connection.session.commit()
                return True
            except:
                return False
            finally:
                connection.session.close()
