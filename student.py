from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.database import SessionLocal
from app.models import QuestionPaper
from app.schema import QuestionPaperResponse

router = APIRouter(prefix="/student", tags=["Student"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get(
    "/papers/{subject_id}",
    response_model=List[QuestionPaperResponse]
)
def get_papers_by_subject(subject_id: int, db: Session = Depends(get_db)):
    papers = (
        db.query(QuestionPaper)
        .filter(QuestionPaper.subject_id == subject_id)
        .order_by(QuestionPaper.year.desc())
        .all()
    )
    return papers
