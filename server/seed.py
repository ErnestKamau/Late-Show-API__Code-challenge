# server/seed.py

from config import app, db
from models import User, Guest, Episode, Appearance
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

with app.app_context():
    print("Seeding database...")

    
    db.drop_all()
    db.create_all()

    #Create a user
    password_hash = bcrypt.generate_password_hash("password123").decode('utf-8')
    user1 = User(username="ernest", _password_hash=password_hash)

    
    guest1 = Guest(name="Trevor Noah", occupation="Comedian")
    guest2 = Guest(name="Bill Gates", occupation="Philanthropist")
    guest3 = Guest(name="Zendaya", occupation="Actress")

    
    episode1 = Episode(date="2024-05-10", number=101)
    episode2 = Episode(date="2024-05-11", number=102)

    
    appearance1 = Appearance(rating=5, guest=guest1, episode=episode1)
    appearance2 = Appearance(rating=4, guest=guest2, episode=episode1)
    appearance3 = Appearance(rating=5, guest=guest3, episode=episode2)

    
    db.session.add_all([
        user1,
        guest1, guest2, guest3,
        episode1, episode2,
        appearance1, appearance2, appearance3
    ])

    
    db.session.commit()
    print("Done seeding!")
