from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    email: str

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email: str
    password: str

class ResumeResponse(BaseModel):
    id: int
    filename: str

    class Config:
        from_attributes: True

class ResumeAnalysisRequest(BaseModel):
    job_description: str

class AnalysisResponse(BaseModel):
    id: int
    resume_id: int
    job_description: str
    analysis_result: str

    class Config:
        from_attributes = True