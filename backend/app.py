from flask import Flask, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
import yaml

app = Flask(__name__)

# Swagger UI configuration
SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI
API_URL = '/static/openapi.yaml'  # Our API url (can be a local file)

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "ColabDev Open Day Management System API"
    }
)

# Register blueprint at URL
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# Serve OpenAPI spec
@app.route('/static/openapi.yaml')
def serve_swagger_spec():
    with open('openapi.yaml', 'r') as f:
        spec = yaml.safe_load(f)
    return jsonify(spec) 