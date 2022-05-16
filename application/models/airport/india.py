from unicodedata import name
from application.models.base_model import BaseModel
from application import db
from sqlalchemy import func
from geoalchemy2 import Geometry
from geoalchemy2.comparator import Comparator

class IndianAirports(BaseModel):
  """Airports with its geospatial data."""

  __tablename__="indian_airports"

  name  = db.Column(db.String(255))
  longitude = db.Column(db.Float)
  latitude = db.Column(db.Float)
  geo = db.Column(Geometry(geometry_type="POINT"))

  def __repr__(self):
    return "<Airport {name} ({lat}, {lon})>".format(name=self.name, lat=self.latitude, lon=self.longitude)
  
  
  def get_airports_within_radius(self, radius):
    """Return all airports within a given radius (in meters)."""
    
    return IndianAirports.query.filter(func.ST_Distance_Sphere(IndianAirports.geo, self.geo) < radius).all()

  @classmethod
  def add_airport(cls, name, longitude, latitude):
    """Add a new airport detail in the database."""
    
    geo = 'POINT({} {})'.format(longitude, latitude)
    #geo1 = func.ST_GeomFromText(geo,4326)
    airport_detail = IndianAirports(name=name, longitude=longitude, latitude=latitude, geo=geo)

    db.session.add(airport_detail)
    db.session.commit()
  
  @classmethod
  def update_geometries(cls):
    """Using each airports longitude and latitude, add geometry data to db."""
    
    airports = IndianAirports.query.all()
    for airport in airports:
      point = 'POINT({} {})'.format(airport.longitude, airport.latitude)
      airport.geo = point
    
    db.session.commit()
  

  @classmethod
  def get_nearest_loc(cls, lon, lat):
    """Find the nearest airport from the netered location.

    Args:
        lon (float): Longitude
        lat (float): Latitude
    """

    nearest_loc = cls.query.order_by(Comparator.distance_centroid(cls.c.geo, 
                  func.Geometry(func.ST_GeographyFromText('POINT({} {})'.format(lon, lat))))).limit(1).first()
    
    return nearest_loc
  
  @classmethod
  def get_all(cls):
    """Get all airport details"""
    
    return cls.query.all()
    



