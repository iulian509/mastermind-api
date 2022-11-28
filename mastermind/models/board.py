from sqlalchemy.sql import func

from mastermind.common.database import db


class Board(db.Model):
    __tablename__ = "board"
    id = db.Column(db.Integer, primary_key=True)
    guess = db.Column(db.String())
    game = db.Column(db.ForeignKey("game.id"), nullable=True)
    black_pegs = db.Column(db.Integer())
    white_pegs = db.Column(db.Integer())
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __init__(self, guess, game, black_pegs, white_pegs):
        self.guess = guess
        self.game = game
        self.black_pegs = black_pegs
        self.white_pegs = white_pegs
