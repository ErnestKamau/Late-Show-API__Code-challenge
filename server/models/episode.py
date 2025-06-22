from sqlalchemy_serializer import SerializerMixin
from config import db


class Episode(db.Model, SerializerMixin):
    __tablename__ = 'episodes'
    
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String, nullable=False)
    number = db.Column(db.Integer, nullable=False)
    
    appearances = db.relationship('Appearance', back_populates='episode', cascade="all, delete")
    
    
    def __repr__(self):
        return f"<Episode #{self.number} on {self.date}>"
    