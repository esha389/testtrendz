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

Features:
Admin-only upload of question papers
Subject-wise and year-wise question storage
Repeated topic and trend analysis
Graphical visualization of important topics
Probability-based question prediction (non-guaranteed)
Desktop application interface

Tech Stack:
Frontend
React.js
Electron (desktop wrapper)
Backend
FastAPI (Python)
SQLAlchemy ORM
Database
PostgreSQL
Analytics / AI
Python (Pandas, Scikit-learn)
Tools
VS Code
Postman
Git & GitHub

System Architecture (High Level):
Admin uploads question data
Backend stores structured data in PostgreSQL
Analytics engine processes frequency and trends
Prediction logic ranks high-probability questions
Frontend displays insights, graphs, and resources

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

Project Status:
✅ Backend setup complete
✅ Database integration completed
🚧 Analytics APIs in progress
🚧 Frontend development in progress

Author:
Developed a Project to demonstrate full-stack development, data analytics, and practical AI application.


Scalable backend architecture
