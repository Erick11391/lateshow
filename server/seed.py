from app import app, db
from models import Episode, Guest, Appearance
from faker import Faker
import csv
import random

fake = Faker()

def seed_data():
    with app.app_context():
        # Clear existing data
        Appearance.query.delete()
        Episode.query.delete()
        Guest.query.delete()

        # Seed episodes with Faker
        episodes = []
        for _ in range(10):
            episode = Episode(
                date=fake.date_this_century().strftime("%-m/%-d/%y"),  # format like "1/12/99"
                number=random.randint(1, 100)
            )
            db.session.add(episode)
            episodes.append(episode)
        
        db.session.commit()

        # Seed guests from CSV
        guests = []
        with open('guests.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                guest = Guest(name=row['name'], occupation=row['occupation'])
                db.session.add(guest)
                guests.append(guest)
        
        db.session.commit()

        # Create appearances
        for _ in range(50):
            appearance = Appearance(
                rating=random.randint(1, 5),
                episode_id=random.choice(episodes).id,
                guest_id=random.choice(guests).id
            )
            db.session.add(appearance)
        
        db.session.commit()
        print("✅ Database seeded successfully.")

if __name__ == "__main__":
    seed_data()
