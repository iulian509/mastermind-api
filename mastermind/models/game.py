from sqlalchemy.sql import func

from mastermind.common.database import db


class Game(db.Model):
    __tablename__ = "game"
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String())
    max_tries = db.Column(db.Integer())
    solved = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __init__(self, code, max_tries):
        self.code = code
        self.max_tries = max_tries
