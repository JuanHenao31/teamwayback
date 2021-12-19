from flask import Flask

from app.modules.answer import register_answer_routes
from app.modules.question import register_question_routes
from app.modules.result import register_result_routes


def register_routes(app: Flask):
    app.add_url_rule(
        "/", view_func=lambda: {'message': 'application is working perfectly'})
    register_question_routes(app)
    register_answer_routes(app)
    register_result_routes(app)
