import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))  # project root

class Config:   
    INSTANCE_PATH = os.path.join(BASE_DIR, "instance")
    if not os.path.exists(INSTANCE_PATH):
        os.makedirs(INSTANCE_PATH)

    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(INSTANCE_PATH, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
