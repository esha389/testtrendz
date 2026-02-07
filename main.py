from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os

from app.database import engine
from app.models import Base
from app.routes import admin, analytics, student

app = FastAPI(title="TestTrendz")

# -----------------------------
# Ensure uploads directory exists
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)

# -----------------------------
# Static files
# -----------------------------
app.mount("/uploads", StaticFiles(directory=UPLOAD_DIR), name="uploads")

# -----------------------------
# Middleware
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Routers
# -----------------------------
app.include_router(admin.router)
app.include_router(analytics.router)
app.include_router(student.router)

# -----------------------------
# Database tables
# -----------------------------
Base.metadata.create_all(bind=engine)

# -----------------------------
# Root
# -----------------------------
@app.get("/")
def root():
    return {"message": "Backend running successfully"}
