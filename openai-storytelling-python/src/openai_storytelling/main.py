# filepath: 
# ...existing code...
import os
import sys

# ensure package imports work when running the file directly
_proj_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if _proj_root not in sys.path:
    sys.path.insert(0, _proj_root)

from openai_storytelling.api.routes import api_routes

from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Register API routes
    app.register_blueprint(api_routes)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
# ...existing code...