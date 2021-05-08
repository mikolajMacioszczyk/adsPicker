import flask
from flask import request, jsonify
from services.adsService import AdsService
from db.context import Context


def start():
    app = flask.Flask(__name__)
    app.config['DEBUG'] = True
    adsService = AdsService(Context())

    @app.route('/', methods=['GET'])
    def home():
        return "<p>Api endpoints: </p>" \
               "<ul>" \
               "<li>home: /</li>" \
               "<li>allAds: /api/all?count=[count]</li>" \
               "<li>byId: /api/byId?id=[id]</li>" \
               "<li>byQuery: /api/byQuery?query=[query]&count=[count]&lang=[lang]</li>" \
               "</ul>"

    @app.route('/api/all', methods=['GET'])
    def allAds():
        if 'count' in request.args:
            count = int(request.args['count'])
        else:
            count = 100
        return jsonify([ad.__repr__() for ad in adsService.getAny(count)])

    @app.route('/api/byId', methods=['GET'])
    def byId():
        if 'id' in request.args:
            adId = int(request.args['id'])
        else:
            return "Error: No id field provided. Please specify an id."
        return jsonify(adsService.getById(adId).__repr__())

    @app.route('/api/byQuery', methods=['GET'])
    def byQuery():
        if 'query' in request.args:
            query = request.args['query']
        else:
            return "Error: No query field provided. Please specify a query."
        if 'count' in request.args:
            count = int(request.args['count'])
        else:
            count = 1
        if 'lang' in request.args:
            lang = request.args['lang']
        else:
            lang = 'pl'

        return jsonify([ad.__repr__() for ad in adsService.getByTags(query, count, lang)])

    app.run()


if __name__ == '__main__':
    start()
