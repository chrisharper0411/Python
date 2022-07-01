# continuous_resource_blueprint.py

from flask import Blueprint, request, jsonify
from daos.continuous_resource_dao import ContinuousResourceDao

def create_continuous_resource_blueprint(blueprint_name: str, resource_type: str, resource_prefix: str) -> Blueprint:
    """
    blueprint_name: name of the blueprint, used by Flask for routing
    resource_type: name of the specific type of interval resource, such as Car
    resource_prefix: the plural resource to be used in the api endpoint, such as cars, resulting in "/cars"
    """
    blueprint = Blueprint(blueprint_name, __name__)

    @blueprint.route(f'/{resource_prefix}', methods=["POST"])
    def create_resource():
        resource = ContinuousResourceDao.create_resource(
            resource_type=resource_type,
            name=request.get_json(force=True)['name']
        )
        return jsonify({}), 201

    @blueprint.route(f'/{resource_prefix}', methods=["GET"])
    def get_resources():
        resources = ContinuousResourceDao.get_resources(resource_type=resource_type)
        return jsonify({}), 200

        # Then all the other endpoints
        ...

    return blueprint