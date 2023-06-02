import sys

from flask import Flask
from flask_restful import Api, Resource, marshal_with
import datetime
from models import WebCalendarModel, db
from serialization import WebCalendarDao, resource_fields
from parsers import parser

app = Flask(__name__)
app.config.from_pyfile('app_settings.py')
db.init_app(app)
api = Api(app)

with app.app_context():
    db.drop_all()
    db.create_all()


class WebCalendarEventsToday(Resource):
    @marshal_with(resource_fields)
    def get(self):
        today_events = WebCalendarModel.query.filter(WebCalendarModel.date == datetime.date.today()).all()
        if today_events:
            print('TRYING TO RETURN TODAY EVENTS')
            return [WebCalendarDao(event=event.event, date=event.date, event_id=event.id) for event in today_events]


class WebCalendarEventsAll(Resource):
    @marshal_with(resource_fields)
    def get(self, **kwargs):
        print('TRYING TO RETURN ALL EVENTS')
        all_events = [WebCalendarDao(event=event.event, date=event.date, event_id=event.id) for event in
                      WebCalendarModel().query.all()]
        return all_events

    def post(self):
        args = parser.parse_args()
        new_event = WebCalendarModel(event=args['event'], date=args['date'])
        print('TRYING TO ADD EVENT')

        db.session.add(new_event)
        db.session.commit()
        return {'message': 'The event has been added!', 'event': args['event'], 'date': str(args['date'].date())}, 200


api.add_resource(WebCalendarEventsToday, '/event/today')
api.add_resource(WebCalendarEventsAll, '/event')

# do not change the way you run the program
if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg_host, arg_port = sys.argv[1].split(':')
        app.run(host=arg_host, port=arg_port)
    else:
        app.run()
