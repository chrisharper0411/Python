# continuous_resource.py

from database import db
import datetime

class ContinuousResource(db.Model):
    __tablename__ = "continous_resources" # Specified instead of using the default

    id = db.Column(db.String(36), primary_key=True, unique=True)
    name = db.Column(db.String(36), primary_key=True, unique=True) # Eg Car1
    resource_type = db.Column(db.String(36), primary_key=True) # Car/Lorry/Truck
    created = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)

    # Children
    allocations = db.relationship("ContinuousResourceAllocation", back_populates="resource", lazy=True)