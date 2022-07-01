from flask import Blueprint

def create_continuous_resource_blueprint(blueprint_name: str, resource_type: str, resource_prefix: str) -> Blueprint:
    """
    blueprint_name: name of the blueprint, used by Flask for routing
    resource_type: name of the specific type of interval resource, such as Car or Lorry
    resource_prefix: the plural resource to be used in the api endpoint, such as cars, resulting in "/cars"
    """
    blueprint = Blueprint(blueprint_name, __name__)

    @blueprint.route(f'/{resource_prefix}', methods=["POST"])
    def create_resource():
        return jsonify({}), 201

    @blueprint.route(f'/{resource_prefix}', methods=["GET"])
    def get_resources():
        return jsonify({}), 201

    # We then do this for all the other endpoints we listed
    ...

    return blueprint