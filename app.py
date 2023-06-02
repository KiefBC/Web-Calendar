import sys

from flask import Flask
from flask_restful import Api
from models import db
from resources import WebCalendarEventsToday, WebCalendarEventsAll, WebCalendarByID

app = Flask(__name__)
app.config.from_pyfile('app_settings.py')
api = Api(app)
with app.app_context():
    db.init_app(app)
    db.drop_all()
    db.create_all()


api.add_resource(WebCalendarEventsToday, '/event/today')
api.add_resource(WebCalendarEventsAll, '/event')
api.add_resource(WebCalendarByID, '/event/<int:event_id>')

# do not change the way you run the program
if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg_host, arg_port = sys.argv[1].split(':')
        app.run(host=arg_host, port=arg_port)
    else:
        app.run()
