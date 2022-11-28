from flask import Flask

from mastermind.blueprints.status import status_bp


def create_app():
    flask_app = Flask(__name__, instance_relative_config=True)
    flask_app.register_blueprint(status_bp)

    return flask_app


app = create_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
