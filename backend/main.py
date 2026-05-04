from fastapi import FastAPI

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