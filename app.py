from flask import Flask
from flask_restful import Api
from api import WebCalendar

import sys

app = Flask(__name__)
app.config.update({
    'DEBUG': True,
    'TESTING': True
})
api = Api(app)


api.add_resource(WebCalendar, '/event/today', '/event')

# do not change the way you run the program
if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg_host, arg_port = sys.argv[1].split(':')
        app.run(host=arg_host, port=arg_port)
    else:
        app.run()
