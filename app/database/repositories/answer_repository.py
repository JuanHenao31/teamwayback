from app.database.config.db_connection import DBConnection
from app.database.tables.answer import AnswerModel
from app.domain.model.entity.answer import Answer
from app.domain.ports.repository.repository_answer import RepositoryAnswer


class AnswerRepository(RepositoryAnswer):

    def create(self, answer: Answer) -> int:
        answer_params: Answer = answer

        with DBConnection() as connection:
            try:
                answer_to_save = AnswerModel(
                    content=answer_params.content,
                    weight=answer_params.weight,
                    question_id=answer_params.question_id
                )
                connection.session.add(answer_to_save)
                connection.session.commit()
                connection.session.flush()
                return answer_to_save.to_core_model()
            except:
                connection.session.rollback()
                raise Exception('Error on save Answer')
            finally:
                connection.session.close()

    def update(self, answer_id: int, answer: Answer):
        with DBConnection() as connection:
            try:
                answer_in_database = connection.session.query(
                    AnswerModel).filter_by(id=answer_id).first()

                answer_in_database.content = answer.content
                answer_in_database.answer = answer.answer

                connection.session.commit()
                return answer_in_database.to_core_model()
            except:
                return None
            finally:
                connection.session.close()

    def delete(self, id: int):
        with DBConnection() as connection:
            try:
                answer_in_database = connection.session.query(
                    AnswerModel).filter_by(id=id).delete()
                connection.session.commit()
                return True
            except:
                return False
            finally:
                connection.session.close()
