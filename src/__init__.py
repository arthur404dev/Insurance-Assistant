from flask import Flask

# Define App Creator ->


def create_app():
    # Create server entity
    app = Flask(__name__)
    # Link Config File
    app.config.from_pyfile('config.py')
    # Create Sanity Check Route
    @app.route('/')
    def index():
        return f'MONGO_URI = {app.config.get("MONGO_URI")}'

    # Create server runner
    if __name__ == '__main__':
        app.run(debug=True)

    # Return creator
    return app
