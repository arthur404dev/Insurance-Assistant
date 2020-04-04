# App Constructors
from flask import Flask, jsonify, request
# Module imports
from app.database import init_database
from app.controllers.application import post_application
from app.scripts import evaluateRisk
# Define App Creator ->


def create_app():
    # Create server entity
    app = Flask(__name__)
    # Link Config File
    app.config.from_pyfile('config.py')
    # Initialize Databases
    db = init_database(app)
    # Initialize Routes: (Not going to use folder for routing as they're too few)
    @app.route('/')
    def index():
        return jsonify({'status': 'App Running'})

    @app.route('/risk')
    def risk():
        return evaluateRisk()

    @app.route("/api/user/application", methods=['POST'])
    def post():
        return post_application(db)

    # Create server runner
    if __name__ == '__main__':
        app.run(debug=True)
    # Return creator
    return app
