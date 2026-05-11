# AI Resume Analyser Backend 🤖

A production-style backend project for an AI-powered resume analysis platform built with:

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy ORM
* OpenAI API
* PDF text extraction

This project allows users to:

* Upload resumes
* Extract text from PDFs
* Store resumes in PostgreSQL
* Analyze resumes against job descriptions using AI
* Store analysis history
* Retrieve analyses
* Delete resumes and analyses

---

# Features ⚙️

## Authentication 

* User registration
* User login
* Password hashing with bcrypt
* Secure password verification

---

## Resume Management 

* Upload PDF resumes
* Extract text from uploaded resumes
* Save extracted text to PostgreSQL
* Retrieve all resumes
* Retrieve a specific resume
* Delete resumes

---

## AI Resume Analysis 

* Compare resume against job description
* Generate:

  * Match score
  * Strengths
  * Missing skills
  * Improvement suggestions
  * ATS optimization feedback
  * Suggested keywords

---

## Database Features 

* PostgreSQL integration
* SQLAlchemy ORM models
* Table relationships
* Cascade deletion
* Persistent analysis history

---

# Tech Stack 

| Technology    | Purpose               |
| ------------- | --------------------- |
| Python        | Backend language      |
| FastAPI       | API framework         |
| PostgreSQL    | Relational database   |
| SQLAlchemy    | ORM                   |
| Pydantic      | Data validation       |
| OpenAI API    | AI analysis           |
| PyPDF2        | PDF text extraction   |

---

# Project Structure 🏗️

```text
backend/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── auth.py
├── ai.py
├── requirements.txt
├── .env
├── .gitignore
├── uploads/
│
└── venv/
```

---

# API Architecture 📡

```text
Frontend/User
        ↓
FastAPI Backend
        ↓
Business Logic
        ↓
SQLAlchemy ORM
        ↓
PostgreSQL Database
```

# Installation ⬇️

## 1. Clone Repository

```bash
git clone <repo-url>
cd ai-resume-interview-assistant/backend
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

### macOS/Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Setup PostgreSQL

Install PostgreSQL and create a database user.

Example:

```sql
CREATE USER alwn WITH PASSWORD 'password';
ALTER USER alwn CREATEDB;
```

---

## 5. Create Tables

```bash
python create_tables.py
```

---

## 6. Run Backend Server

```bash
uvicorn main:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

---


# SQLAlchemy Concepts Used

## ORM

Instead of writing raw SQL queries everywhere, SQLAlchemy ORM maps Python classes to database tables.

Example:

```python
class Resume(Base):
```

maps to:

```sql
resumes table
```

---

## Sessions

Database sessions are used to communicate with PostgreSQL.

Pattern used throughout the project:

```python
db = SessionLocal()

# database work

db.close()
```

---

## Relationships

```python
relationship()
```

Used to create links between models.

Example:

```text
Resume → Analyses
```

---

## Cascade Delete

```python
cascade="all, delete-orphan"
```

Automatically deletes analyses when a resume is deleted.

---

# AI Integration

The backend uses the OpenAI Python SDK.

Flow:

```text
Resume Text
+ Job Description
→ OpenAI API
→ AI Analysis
→ Store Result
```

The AI logic is separated into:

```text
ai.py
```

This keeps:

* API routing
* database logic
* AI logic

properly separated.

---

# Security Notes

* Passwords are hashed using bcrypt
* API keys stored in `.env`
* `.env` should never be committed to GitHub
* Database credentials are environment-based

---

# Future Improvements

## Backend

* JWT authentication
* User-specific resumes
* Async background processing
* Resume versioning
* Pagination
* Docker support
* Redis caching
* Celery task queue
* Unit testing
* Logging
* Rate limiting

---

## AI Features

* ATS scoring engine
* Structured JSON AI responses
* Embeddings + semantic matching
* Multi-model support
* Open-source LLM integration
* Resume rewriting
* Interview question generation

---

## Frontend

Potential frontend stack:

* React
* Next.js
* Tailwind CSS
* Axios

Possible UI features:

* Dashboard
* Resume upload UI
* Analysis history
* AI feedback cards
* ATS score visualization

---

# Learning Outcomes

This project demonstrates:

* Backend API development
* Database design
* ORM relationships
* Authentication systems
* File upload handling
* AI integration architecture
* Environment configuration
* REST API design
* Error handling
* Real-world debugging

---

# Notes

This project was intentionally built in a layered architecture:

```text
Routes
→ Services
→ Database
→ External APIs
```

This structure scales much better than putting all logic inside a single file.

---

# License

MIT License
