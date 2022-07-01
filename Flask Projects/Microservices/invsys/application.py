from flask import Flask
from blueprints.continuous_resource_blueprint import create_continuous_resource_blueprint

def create_app() -> Flask:
    app = Flask(__name__)

    # Register continuous resource blueprints
    app.register_blueprint(
        create_continuous_resource_blueprint(
            blueprint_name="CarsBlueprint", # The name, used by flask when using the url_for function
            resource_type="Car", # The resource type
            resource_prefix="cars" # The base of the url for this resource type
        ),
        url_prefix='/api'
    )

    # Then do the same for lorry and truck
    ...

    return app