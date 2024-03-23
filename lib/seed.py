#!/usr/bin/env python3

from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Game

fake = Faker()

if __name__ == '__main__':
    # Create a database engine
    engine = create_engine('sqlite:///seed_db.db')
    
    # Create a session class
    Session = sessionmaker(bind=engine)
    
    # Create a session
    session = Session()
    
    # Delete existing Game records
    session.query(Game).delete()
    session.commit()
    
    # Add a console message so we can see output when the seed file runs
    print("Seeding games...")
    
    # Generate fake data and insert into the database
    games = [
        Game(
            title=fake.name(),
            genre=fake.word(),
            platform=fake.word(),
            price=random.randint(0, 60)
        )
        for _ in range(50)
    ]
    
    session.bulk_save_objects(games)
    session.commit()
