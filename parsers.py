from flask_restful import reqparse, inputs

parser = reqparse.RequestParser()
parser.add_argument('date', type=inputs.date,
                    help='The event date with the correct format is required! The correct format is YYYY-MM-DD!',
                    required=True)
parser.add_argument('event', type=str, help='The event name is required!', required=True)