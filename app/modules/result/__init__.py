from flask import Flask

from app.modules.result.controllers.list_a_result import list_a_result


def register_result_routes(app: Flask):

    # Get A Result
    app.add_url_rule('/result-list', view_func=list_a_result, methods=['GET'])
