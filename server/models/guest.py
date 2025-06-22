from sqlalchemy_serializer import SerializerMixin
from config import db

class Guest(db.Model, SerializerMixin):
    __tablename__ = 'guests'
   
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    occupation = db.Column(db.String, nullable=False)
    
    appearances = db.relationship("Appearance", backref="guest", cascade="all, delete")
    
    
    def __repr__(self):
        return f'<Geust {self.id} : name={self.name}, occupation={self.occupation}>'
    
