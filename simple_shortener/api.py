from flask_restful import Api, Resource, reqparse
from flask import redirect

from simple_shortener import app

api = Api(app)


class ShortenUrl(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('url', required=True, help='Missing Url to shorten')

    def post(self):
        args = self.parser.parse_args(strict=True)

        # ToDo

        return {'shortened_url': 'ToDo'}, 201


class Redirect(Resource):
    def get(self, alias):

        # ToDo

        return redirect("https://www.google.com/", code=301)


api.add_resource(ShortenUrl, '/shorten_url')
api.add_resource(Redirect, '/<alias>')