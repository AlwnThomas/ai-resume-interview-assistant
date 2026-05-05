from fastapi import FastAPI, HTTPException, File, UploadFile
from PyPDF2 import PdfReader
from schemas import UserCreate, UserResponse, UserLogin, ResumeResponse
from sqlalchemy.exc import IntegrityError
from models import User, Resume
from database import SessionLocal
from auth import hash_password, verify_password
import io

app = FastAPI(
    title="AI Resume & Interview Assistant",
    version="0.1.0"
)

@app.get("/")
def root():
    return{"message": "AI Resume & Interview Assistant API"}

@app.get("/health")
def health_check():
    return{"status": "ok"}

@app.post("/users")
def create_user(user: UserCreate):

    db = SessionLocal()

    new_user = User(
        email=user.email,
        hashed_password=hash_password(user.password)
    )

    try:
        db.add(new_user)
        db.commit()

    except IntegrityError:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )
    
    finally:
        db.close()

    return {"message": "User created successfully"}

@app.get("/users", response_model=list[UserResponse])
def get_users():

    db = SessionLocal()

    users = db.query(User).all()

    db.close()

    return users

@app.post("/login")
def login(user: UserLogin):

    db = SessionLocal()

    existing_user = db.query(User).filter(User.email == user.email).first()

    db.close()

    if existing_user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )
    
    if not verify_password(user.password, existing_user.hashed_password):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )
    
    return {"message": "Login Successful"}

@app.post("/resume/upload")
async def upload_resume(file: UploadFile = File(...)):

    contents = await file.read()

    pdf_file = io.BytesIO(contents)

    reader = PdfReader(pdf_file)

    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    db = SessionLocal()

    new_resume = Resume(
        filename=file.filename,
        extracted_text=text
    )

    db.add(new_resume)
    db.commit()
    db.close()

    return{
        "message": "Resume uploaded successfully",
        "filename": file.filename
    }

@app.get("/resumes", resume_model=list[ResumeResponse])
def get_resumes():

    db = SessionLocal()

    resumes = db.query(Resume).all()

    db.close()

    return resumes