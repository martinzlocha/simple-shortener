from flask_restful import Api, Resource, reqparse
from flask import redirect, request

from simple_shortener import app, db, cache
from simple_shortener.alias_mapper import AliasMapper

api = Api(app)
alias_mapper = AliasMapper(db)


class ShortenUrl(Resource):
    def __init__(self):
        self._parser = reqparse.RequestParser()
        self._parser.add_argument('url', required=True, help='Missing Url to shorten')

    def post(self):
        args = self._parser.parse_args(strict=True)
        alias = alias_mapper.store_url(args['url'])
        return {'shortened_url': '{}{}'.format(request.host_url, alias)}, 201


class Redirect(Resource):
    @cache.cached(timeout=app.config['CACHE_DURATION'])
    def get(self, alias):
        try:
            return redirect(alias_mapper.get_url(alias), code=301)
        except KeyError:
            return 'Could not find a target for the provided url.', 404


api.add_resource(ShortenUrl, '/shorten_url')
api.add_resource(Redirect, '/<alias>')