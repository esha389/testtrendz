# app/routes/admin.py
from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session
import os
from typing import List
from app.database import SessionLocal
from app.models import Question, QuestionPaper
from app.schema import SubjectCreate, SubjectResponse, QuestionPaperResponse
from app.crud import (
    get_all_subjects,
    create_subject,
    insert_parsed_questions,
    get_all_question_papers,
)
from app.utils.ocr import extract_text_from_image
from app.utils.parser import parse_question_paper

router = APIRouter(prefix="/admin", tags=["Admin"])


# -----------------------------
# DB dependency
# -----------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# -----------------------------
# Upload directory
# -----------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.get("/papers/{subject_id}")
def get_papers_by_subject(subject_id: int, db: Session = Depends(get_db)):
    papers = (
        db.query(QuestionPaper)
        .filter(QuestionPaper.subject_id == subject_id)
        .all()
    )

    return [
        {
            "id": p.id,
            "subject_id": p.subject_id,
            "year": p.year,
            "exam_type": p.exam_type,
            "image_path": p.image_path,  # IMPORTANT
        }
        for p in papers
    ]
# -----------------------------
# SUBJECT APIs
# -----------------------------
@router.get("/subjects")
def list_subjects(db: Session = Depends(get_db)):
    return get_all_subjects(db)

@router.post("/subjects", response_model=SubjectResponse)
def add_subject(subject: SubjectCreate, db: Session = Depends(get_db)):
    return create_subject(db, subject.name, subject.semester)

# -----------------------------
# LIST PAPERS (ONLY ONE)
# -----------------------------
@router.get("/papers", response_model=List[QuestionPaperResponse])
def list_uploaded_papers(db: Session = Depends(get_db)):
    return get_all_question_papers(db)

# -----------------------------
@router.post("/upload-paper")
def upload_question_paper(
    subject_id: int,
    year: int,
    exam_type: str,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    # 1️⃣ Create year folder
    year_folder = os.path.join(UPLOAD_DIR, str(year))
    os.makedirs(year_folder, exist_ok=True)

    # 2️⃣ Save file to disk (absolute path)
    file_path = os.path.join(year_folder, file.filename)
    with open(file_path, "wb") as f:
        f.write(file.file.read())

    print(f"✅ File saved at: {file_path}")

    # 3️⃣ Store RELATIVE path in DB
    relative_path = f"/uploads/{year}/{file.filename}"

    # 4️⃣ OCR
    text = extract_text_from_image(file_path)
    print("\n========== OCR TEXT ==========")
    print(text)

    # 5️⃣ Parse questions
    parsed_questions = parse_question_paper(
        text=text,
        subject="AUTO",
        year=year,
    )

    print("\n========== PARSED QUESTIONS ==========")
    print(parsed_questions)

    # 6️⃣ Create paper (ONLY ONCE)
    paper = QuestionPaper(
        subject_id=subject_id,
        year=year,
        exam_type=exam_type,
        image_path=relative_path,
    )
    db.add(paper)
    db.commit()
    db.refresh(paper)

    print(f"✅ Paper created with ID: {paper.id}")

    # 7️⃣ Insert parsed questions
    insert_parsed_questions(
        db=db,
        questions=parsed_questions,
        paper_id=paper.id,
    )

    return {
        "message": "Question paper uploaded successfully",
        "paper_id": paper.id,
        "questions_inserted": len(parsed_questions),
    }


# -----------------------------
# ADD SINGLE QUESTION
# -----------------------------
@router.post("/add-question")
def add_question(
    subject_id: int,
    year: int,
    exam_type: str,
    unit: str,
    question_text: str,
    marks: int,
    db: Session = Depends(get_db),
):
    paper = QuestionPaper(
        subject_id=subject_id,
        year=year,
        exam_type=exam_type,
    )
    db.add(paper)
    db.commit()
    db.refresh(paper)

    question = Question(
        paper_id=paper.id,
        unit=unit,
        question_text=question_text,
        marks=marks,
    )
    db.add(question)
    db.commit()

    return {"message": "Question added successfully"}


# -----------------------------
# UPDATE QUESTION
# -----------------------------
@router.put("/update-question/{question_id}")
def update_question(
    question_id: int,
    question_text: str | None = None,
    unit: str | None = None,
    marks: int | None = None,
    db: Session = Depends(get_db),
):
    question = db.query(Question).filter(Question.id == question_id).first()

    if not question:
        return {"error": "Question not found"}

    if question_text is not None:
        question.question_text = question_text
    if unit is not None:
        question.unit = unit
    if marks is not None:
        question.marks = marks

    db.commit()
    return {"message": "Question updated successfully"}
# URL path to be stored in DB (NOT disk path)



