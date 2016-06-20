from flask import Flask
from data import get_epitet, add_name
from flask.ext.cors import CORS
from flask_restful import Resource, Api

app = Flask(__name__)
CORS(app)
api = Api(app)


class NiceForm(Resource):
    def get(self, name):
        try:
            data = get_epitet(name)
        except TypeError:
            add_name(name)
            data = get_epitet(name)
        finally:
            return {'epitet': data, 'name':name}
 
api.add_resource(NiceForm, '/<string:name>')

if __name__ == "__main__":
    app.run(debug=True)
