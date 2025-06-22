from sqlalchemy_serializer import SerializerMixin
from config import db

class Appearance(db.Model, SerializerMixin):
    __tablename__ = 'appearances'

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)

    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'), nullable=False)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), nullable=False)

    

    def __repr__(self):
        return f"<Appearance GuestID={self.guest_id} EpisodeID={self.episode_id} Rating={self.rating}>"
    
    