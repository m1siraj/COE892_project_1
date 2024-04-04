from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

class Warehouse(Base):
    __tablename__ = 'warehouses'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    latitude = Column(Float)
    longitude = Column(Float)
    max_capacity = Column(Integer)
    current_capacity = Column(Integer)

class DeliveryVehicle(Base):
    __tablename__ = 'delivery_vehicles'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    range = tuple(Integer, Integer)
    capacity = Column(Integer)
    
