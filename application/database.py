from flask_sqlalchemy import SQLAlchemy


class Config:
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = None

class LocalDevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///TicketTales.sqlite3'


db = SQLAlchemy()