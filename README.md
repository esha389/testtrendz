# testtrendz
TestTrendz is a desktop-based exam analytics and prediction platform that centralizes BCA question papers, analyzes topic trends, and highlights high-probability questions using data analytics and AI techniques.

Problem Statement

As a student, preparing for exams requires going through multiple sources of previous year question papers and model papers.
There is no single platform that:

Stores question papers year-wise and subject-wise
Identifies repeated and high-weightage topics
Provides data-driven insights on likely questions
Links important topics to relevant learning resources
This makes exam preparation time-consuming and inefficient

Solution:
TestTrendz solves this problem by providing:
A centralized repository for exam question papers
Topic-wise and year-wise analysis
Frequency-based importance scoring
Probability-based question prediction
Visual analytics for better understanding
Curated YouTube resources for high-importance topics

Key Features

Subject-wise question paper repository
AI-style topic prediction based on historical trends
Interactive bar-chart analytics dashboard
Complete syllabus topic visualization
Admin panel for paper upload & management
Modern glassmorphism UI with gradient analytics

Tech Stack
Frontend
React (Vite)
Tailwind CSS
Chart.js / Recharts
React Router

Backend
FastAPI (Python)
Postgre SQL / structured storage
Image upload & static serving


System Architecture

Admin Upload → Backend Storage → Topic Weight Mapping → Prediction Engine → Visual Dashboard → Student Access

Project structure:
testtrendz/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── database.py
│   │   ├── models.py
│   │   ├── analytics.py
│   │   ├── prediction.py
│   │   └── routes/
│   │       └── admin.py
│   └── requirements.txt
│
├── frontend/   (React – upcoming)
├── electron/   (Desktop wrapper – upcoming)
└── README.md

cd backend
venv\Scripts\activate
python -m uvicorn app.main:app --reload
Open in browser:
http://127.0.0.1:8000
http://127.0.0.1:8000/docs

Initial project setup with React frontend and FastAPI backend

