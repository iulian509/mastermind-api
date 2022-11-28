from flask import Flask

from mastermind.blueprints.status import status_bp
from mastermind.blueprints.game import game_bp
from mastermind.common.database import db, init_db
from mastermind.common.errors import setup_errors


def create_app():
    flask_app = Flask(__name__, instance_relative_config=True)
    flask_app.config.from_object("settings.ProductionConfig")
    flask_app.register_blueprint(status_bp)
    flask_app.register_blueprint(game_bp)
    db.init_app(flask_app)
    init_db(flask_app)

    return flask_app


app = create_app()
setup_errors(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
