"""
This script runs the ImagePreprocessingAPI application using a development server.
"""

# from os import environ
from ImagePreprocessingAPI import app

if __name__ == '__main__':
    app.run()
    # HOST = 'localhost'
    # PORT = 5030
    # HOST = environ.get('SERVER_HOST', 'localhost')
    # try:
    #     PORT = int(environ.get('SERVER_PORT', '5555'))
    # except ValueError:
    #     PORT = 5555
    # app.run(HOST, PORT)
