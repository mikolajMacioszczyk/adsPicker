import flask
from flask import request, jsonify
from services.adsService import AdsService
from services.imageService import ImageService
from db.context import Context
import cv2
import base64
from flask_cors import CORS
from services.wordService import WordService


def start():
    app = flask.Flask(__name__)
    CORS(app)
    app.config['DEBUG'] = True
    wordService = WordService()
    adsService = AdsService(Context(), wordService)
    imageService = ImageService()

    @app.route('/', methods=['GET'])
    def home():
        return "<p>Api endpoints: </p>" \
               "<ul>" \
               "<li>home: /</li>" \
               "<li>all ads: /api/all?count=[count]</li>" \
               "<li>ad by Id: /api/byId?id=[id]</li>" \
               "<li>create ad: /api/create</li>" \
               "<li>update ad: /api/update?id=[id]</li>" \
               "<li>remove ad: /api/remove?id=[id]</li>" \
               "<li>upload image: /api/image/upload</li>" \
               "<li>ad image by id: /api/image/byId?id=[id]</li>" \
               "<li>ads by query: /api/byQuery?query=[query]&count=[count]&lang=[lang]</li>" \
               "</ul>"

    @app.route('/api/all', methods=['GET'])
    def allAds():
        if 'count' in request.args:
            count = int(request.args['count'])
        else:
            count = 100
        response = jsonify([ad.__repr__() for ad in adsService.getAny(count)])
        return response

    @app.route('/api/byId', methods=['GET'])
    def byId():
        if 'id' in request.args:
            adId = int(request.args['id'])
        else:
            return "Error: No id field provided. Please specify an id."
        response = jsonify(adsService.getById(adId).__repr__())
        return response

    @app.route('/api/create', methods=['POST'])
    def createAd():
        title, description = request.json.get('title'), request.json.get('description')
        imagePath, tags = request.json.get('imagePath'), request.json.get('tags')
        response = jsonify(adsService.create(title, description, imagePath, tags).__repr__())
        return response

    @app.route('/api/update', methods=['POST'])
    def updateAd():
        if 'id' in request.args:
            adId = int(request.args['id'])
        else:
            return "Error: No id field provided. Please specify an id."
        title, description = request.json.get('title'), request.json.get('description')
        imagePath, tags = request.json.get('imagePath'), request.json.get('tags')
        response = jsonify(adsService.update(adId, title, description, imagePath, tags).__repr__())
        return response

    @app.route('/api/remove', methods=['POST'])
    def removeAd():
        if 'id' in request.args:
            adId = int(request.args['id'])
        else:
            return "Error: No id field provided. Please specify an id."
        response = jsonify(adsService.remove(adId))
        return response

    @app.route('/api/image/upload', methods=['POST'])
    def uploadImage():
        image = request.files['image']
        path = request.host_url + "api/image?path=" + imageService.saveFileStorage(image)
        response = jsonify(path)
        return response

    @app.route('/api/image', methods=['GET'])
    def getImage():
        if 'path' in request.args:
            path = request.args['path']
        else:
            return "Error: No path field provided. Please specify an path."
        res = imageService.downloadToFlask(path)
        return res

    @app.route('/api/image/byId', methods=['GET'])
    def imageById():
        if 'id' in request.args:
            adId = int(request.args['id'])
        else:
            return "Error: No id field provided. Please specify an id."
        ad = adsService.getById(adId)
        if ad:
            img = imageService.getImage(ad.imagePath)
            _, encoded_img = cv2.imencode('.PNG', img)
            encoded_img = base64.b64encode(encoded_img)
            return encoded_img
        return None

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

        response = jsonify([ad.__repr__() for ad in adsService.getByTags(query, count, lang)])
        return response

    app.run()


if __name__ == '__main__':
    start()
