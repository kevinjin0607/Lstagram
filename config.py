import os

class Config(object):
    # CSRF token
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'