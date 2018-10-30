from flask_restful import Api, Resource, reqparse

from simple_shortener import app

api = Api(app)


parser = reqparse.RequestParser()
parser.add_argument('url', required=True, help='Missing Url to shorten')


class ShortenUrl(Resource):
    def post(self):
        args = parser.parse_args(strict=True)

        # ToDo

        return {'shortened_url': 'ToDo'}, 201


api.add_resource(ShortenUrl, '/shorten_url')