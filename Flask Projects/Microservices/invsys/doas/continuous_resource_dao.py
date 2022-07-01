# continuous_resource_dao.py

from database import db
from typing import List
from models.continuous_resource import ContinuousResource
import uuid

class ContinuousResourceDao:
    @staticmethod
    def create_resource(resource_type, name) -> ContinuousResource:
        resource = ContinuousResource(
            id=str(uuid.uuid4()),
            resource_type=resource_type,
            name=name
        )
        db.session.add(resource)
        db.session.commit()
        return resource

    @staticmethod
    def get_resources(resource_type) -> List[ContinuousResource]:
        return ContinuousResource.query.filter_by(resource_type=resource_type)

    # There will be more functions for each other query
    ...