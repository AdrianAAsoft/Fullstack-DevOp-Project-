from flask import Flask, jsonify
from config import BackendPort
from flask_cors import CORS
from flask_restful import Api
from models import db
from resources import WorkshopListResource, WorkshopResource, WorkshopRegistration, UserRegis, LoginUser

app = Flask(__name__)
app.config.from_object('config.config')
CORS(app) #Habilito CORS para llamadas de front y back en sintonia
api = Api(app)

db.init_app(app)

# Initialize DB
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return jsonify({"message": "Backend Arriba"})

api.add_resource(WorkshopListResource, '/api/workshops')
api.add_resource(WorkshopResource, '/api/workshops/<int:workshop_id>')
api.add_resource(WorkshopRegistration, '/api/workshops/<int:workshop_id>/register')
api.add_resource(UserRegis, '/api/users')
api.add_resource(LoginUser, '/api/login')

if __name__ == '__main__':
    port = int(BackendPort)
    app.run(debug=True, port=port)
