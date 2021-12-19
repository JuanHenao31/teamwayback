from flask import Flask

from app.modules.answer.controllers.save_answer import save_new_answer


def register_answer_routes(app: Flask):

    # insert Answer
    app.add_url_rule('/answer', view_func=save_new_answer, methods=['POST'])
