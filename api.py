from flask_restful import Resource, reqparse, inputs
from flask import make_response

parser = reqparse.RequestParser()
parser.add_argument('date', type=inputs.date,
                    help='The event date with the correct format is required! The correct format is YYYY-MM-DD!',
                    required=True)
parser.add_argument('event', type=str, help='The event name is required!', required=True)


class WebCalendar(Resource):
    def get(self):
        return {'data': 'There are no events for today!'}, 200

    def post(self):
        args = parser.parse_args()
        date_ = args['date']
        name = args['event']

        response_obj = {
            'message': 'The event has been added!',
            'event': name,
            'date': str(date_.date()),
        }
        response = make_response(response_obj, 200)
        return response
