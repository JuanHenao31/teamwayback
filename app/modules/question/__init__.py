from flask import Flask

from app.modules.question.controllers.list_a_question import list_a_question
from app.modules.question.controllers.list_all_question import list_all_question
from app.modules.question.controllers.list_all_question_answer import list_all_question_answer
from app.modules.question.controllers.save_question import save_new_question
from app.modules.question.controllers.save_question_answer import save_new_question_answer


def register_question_routes(app: Flask):
    # insert Question with answers
    app.add_url_rule('/question-answer', view_func=save_new_question_answer, methods=['POST'])

    # insert Question
    app.add_url_rule('/question', view_func=save_new_question, methods=['POST'])

    # Get All Questions
    app.add_url_rule('/question-list', view_func=list_all_question, methods=['GET'])

    # Get A Questions
    app.add_url_rule('/question-list/<int:id>', view_func=list_a_question, methods=['GET'])

    # Get All Questions With it's answers
    app.add_url_rule('/question-answers-list', view_func=list_all_question_answer, methods=['GET'])