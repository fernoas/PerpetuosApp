from src.app import app
from src.controllers.controller import *


HOST = 'localhost'
PORT = 4000
DEBUG = True

if(__name__ == '__main__'):
    app.run(HOST, PORT, DEBUG)

