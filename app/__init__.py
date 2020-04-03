from flask import Flask
from app.database import create_database
# Define App Creator ->


def create_app():
    # Create server entity
    app = Flask(__name__)
    # Link Config File
    app.config.from_pyfile('config.py')
    # Create Sanity Check Route
    @app.route('/')
    def index():
        return f'TestString'
    # Initialize Database
    db = create_database(app)
    # db = create_database(app)
    # Create server runner
    if __name__ == '__main__':
        app.run(debug=True)
    # Return creator
    return app
