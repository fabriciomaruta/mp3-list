from flask import Flask
from flask_restful import Resource, Api
from downloader import Downloader

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')
api.add_resource(Downloader, '/download')

if __name__ == '__main__':
    app.run(debug=True)
