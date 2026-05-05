from database import SessionLocal
from models import User

db = SessionLocal()

new_user = User(
    email="test@example.com",
    hashed_password="fakehashedpassword"
)

db.add(new_user)
db.commit()
db.close()

print("User created successfully!")