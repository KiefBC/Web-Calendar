from flask_restful import reqparse, inputs

parser = reqparse.RequestParser()
parser.add_argument('date', type=inputs.date,
                    help='The event date with the correct format is required! The correct format is YYYY-MM-DD!',
                    required=True)
parser.add_argument('event', type=str, help='The event name is required!', required=True)
parser.add_argument('event_id', type=int, help='The event id is required!', required=False)

parser_timep = reqparse.RequestParser()
parser_timep.add_argument('start_time', type=inputs.date, help='The start time is required!', required=False)
parser_timep.add_argument('end_time', type=inputs.date, help='The end time is required!', required=False)
