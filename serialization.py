from flask_restful import fields


class WebCalendarDao(object):
    def __init__(self, event, date, event_id):
        self.event_id = event_id
        self.event = event
        self.date = date


resource_fields = {
    'id': fields.Integer,
    'event': fields.String,
    'date': fields.String,
}
