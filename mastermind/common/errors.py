from flask import jsonify


def setup_errors(app):
    @app.errorhandler(400)
    def bad_request(err):
        return jsonify({"message": "Bad Request"}), 400

    @app.errorhandler(404)
    def not_found(err):
        return jsonify({"message": "Not Found"}), 404

    @app.errorhandler(500)
    def internal_error():
        return jsonify({"message": "Internal Server Error"}), 500
