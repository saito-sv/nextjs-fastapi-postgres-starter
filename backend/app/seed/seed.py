from sqlalchemy import select
from sqlalchemy.orm import Session
from app.db.session import sync_engine
from app.models.user import User

def seed_user_if_needed():
    with Session(sync_engine) as session:
        with session.begin():
            if session.execute(select(User)).scalar_one_or_none() is not None:
                print("User already exists, skipping seeding")
                return
            print("Seeding user")
            session.add(User(username="Marlon"))
            session.commit()

