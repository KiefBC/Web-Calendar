import datetime

from flask_restful import Resource, marshal_with
from models import WebCalendarModel, db
from serialization import WebCalendarDao
from parsers import parser, parser_timep
from serialization import resource_fields
from flask import abort


class WebCalendarEventsToday(Resource):
    @marshal_with(resource_fields)
    def get(self):
        today = datetime.date.today().strftime("%Y-%m-%d")
        today_events = WebCalendarModel.query.filter(WebCalendarModel.date == today).all()
        if today_events:
            event_list = [WebCalendarDao(event=event.event, date=event.date, event_id=event.id)
                          for event in today_events]
            return event_list
        else:
            abort(404, "There are no events today!")


class WebCalendarEventsAll(Resource):
    @marshal_with(resource_fields)
    def get(self):
        time_period = parser_timep.parse_args()
        start_time = time_period['start_time']
        end_time = time_period['end_time']
        if start_time is None and end_time is None:
            all_events = WebCalendarModel.query.all()
        else:
            all_events = WebCalendarModel.query.filter(WebCalendarModel.date.between(start_time, end_time))
        event_response = [WebCalendarDao(event=event.event, date=event.date, event_id=event.id) for event in all_events]
        return event_response

    @staticmethod
    def post():
        event_info = parser.parse_args()
        event_name = event_info['event']
        event_date = event_info['date'].date()
        db.session.add(WebCalendarModel(event=event_name, date=event_date))
        db.session.commit()
        return {'message': 'The event has been added!', 'event': event_name, 'date': str(event_date)}, 200


class WebCalendarByID(Resource):
    @marshal_with(resource_fields)
    def get(self, event_id):
        event_by_id = WebCalendarModel.query.filter(WebCalendarModel.id == event_id).first()
        if event_by_id:
            event_response = WebCalendarDao(event=event_by_id.event, date=event_by_id.date, event_id=event_by_id.id)
            return event_response
        else:
            abort(404, "The event doesn't exist!")

    @staticmethod
    def delete(event_id):
        delete_event = WebCalendarModel.query.filter_by(id=event_id).first()
        if delete_event:
            db.session.delete(delete_event)
            db.session.commit()
            return {'message': 'The event has been deleted!'}
        else:
            abort(404, "The event doesn't exist!")
