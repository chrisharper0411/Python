from flask import Flask
from blueprints.continuous_resource_blueprint import create_continuous_resource_blueprint
from database import db

def create_app(db_uri: str) -> Flask:
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    # We still need to initialise the db with the flask app, but we can do this after the object has been initialised by using init_app
    db.init_app(app)

    with app.app_context():
        db.create_all()

    # Register cars continuous resource blueprints
    app.register_blueprint(
        create_continuous_resource_blueprint(
            blueprint_name="CarsBlueprint", # The name, used by flask when using the url_for function
            resource_type="Car", # The resource type
            resource_prefix="cars" # The base of the url for this resource type
        ),
        url_prefix='/api'
    )

    # Register lorrys continuous resource blueprints
    app.register_blueprint(
        create_continuous_resource_blueprint(
            blueprint_name="LorrysBlueprint", # The name, used by flask when using the url_for function
            resource_type="Lorry", # The resource type
            resource_prefix="lorrys" # The base of the url for this resource type
        ),
        url_prefix='/api'
    )


    #Register trucks continuous resource blueprints
    app.register_blueprint(
        create_continuous_resource_blueprint(
            blueprint_name="TrucksBlueprint", # The name, used by flask when using the url_for function
            resource_type="Truck", # The resource type
            resource_prefix="trucks" # The base of the url for this resource type
        ),
        url_prefix='/api'
    )

    return app