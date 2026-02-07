# app/crud.py
from sqlalchemy.orm import Session
from app.models import Subject, Question, QuestionPaper, QuestionTopic

# -----------------------------
# SUBJECTS
# -----------------------------
def get_all_subjects(db: Session):
    return db.query(Subject).all()


def create_subject(db: Session, name: str, semester: int):
    subject = Subject(name=name, semester=semester)
    db.add(subject)
    db.commit()
    db.refresh(subject)
    return subject


# -----------------------------
# QUESTION PAPERS
# -----------------------------
def get_all_question_papers(db: Session):
    return (
        db.query(
            QuestionPaper.id,
            QuestionPaper.subject_id,
            Subject.name.label("subject_name"),
            QuestionPaper.year,
            QuestionPaper.exam_type,
            QuestionPaper.image_path,
        )
        .join(Subject, Subject.id == QuestionPaper.subject_id)
        .order_by(QuestionPaper.year.desc())
        .all()
    )


# -----------------------------
# INSERT QUESTIONS + TOPICS
# -----------------------------

def insert_parsed_questions(db, questions, paper_id):
    for q in questions:
        question = Question(
            paper_id=paper_id,
            unit=q.get("unit"),
            question_text=q["question_text"],
            marks=q.get("marks", 0),
        )

        db.add(question)
        db.flush()  # get question.id

       