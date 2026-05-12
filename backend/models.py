from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__="users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    resumes = relationship(
        "Resume",
        back_populates="owner",
        cascade="all, delete-orphan"
    )

class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)
    extracted_text = Column(Text)

    user_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship(
        "User",
        back_populates="resumes"
    )

    analyses = relationship(
        "Analysis", 
        back_populates="resume",
        cascade = "all, delete-orphan"
        )

class Analysis(Base):
    __tablename__ = "analyses"

    id = Column(Integer, primary_key=True, index=True)

    resume_id = Column(Integer, ForeignKey("resumes.id"))

    job_description = Column(Text)
    analysis_result = Column(Text)

    resume = relationship("Resume", back_populates="analyses")