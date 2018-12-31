from flask import Flask, request
from flask_restful import Resource, Api
from utils import predict_flower
import FlowerPredictionNet

app = Flask(__name__)
api = Api(app)

model = FlowerPredictionNet.new()

class FlowerPrediction(Resource):
    def post(self):
        flower_img = request.files['flower_img']
        probs = predict_flower(model, flower_img)
        return probs


api.add_resource(FlowerPrediction, '/pred')

if __name__ == '__main__':
    app.run('0.0.0.0', 80)
