from flask import jsonify


def setup_errors(app):
    @app.errorhandler(400)
    def bad_request(err):
        return jsonify({"message": "Bad Request"}), 400
