from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class WebCalendarModel(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    event = db.Column(db.String(80), nullable=False)
    date = db.Column(db.Date, nullable=False)
