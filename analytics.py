# app/routes/analytics.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Question, QuestionPaper
from collections import defaultdict

router = APIRouter(prefix="/analytics", tags=["Analytics"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/topic-analysis/{subject_id}")
def topic_analysis(subject_id: int, db: Session = Depends(get_db)):
    """
    Unit-based analytics (stable & exam-aligned)

    Returns:
    {
      "overall_units": [ {unit, frequency, percentage} ],
      "by_year": [
        {
          "year": 2024,
          "units": [ {unit, frequency} ]
        }
      ]
    }
    """

    rows = (
        db.query(
            Question.unit,
            QuestionPaper.year
        )
        .join(QuestionPaper, Question.paper_id == QuestionPaper.id)
        .filter(QuestionPaper.subject_id == subject_id)
        .all()
    )

    if not rows:
        return {
            "overall_units": [],
            "by_year": []
        }

    overall = defaultdict(int)
    year_map = defaultdict(lambda: defaultdict(int))
    total = 0

    for unit, year in rows:
        unit = unit.strip() if unit else "Unknown"
        overall[unit] += 1
        year_map[year][unit] += 1
        total += 1

    # overall unit importance
    overall_units = sorted(
        overall.items(),
        key=lambda x: x[1],
        reverse=True
    )

    overall_units = [
        {
            "unit": unit,
            "frequency": freq,
            "percentage": round((freq / total) * 100, 2)
        }
        for unit, freq in overall_units
    ]

    # per-year breakdown
    by_year = []
    for year, units in sorted(year_map.items(), reverse=True):
        by_year.append({
            "year": year,
            "units": [
                {"unit": u, "frequency": f}
                for u, f in sorted(units.items(), key=lambda x: x[1], reverse=True)
            ]
        })

    return {
        "overall_units": overall_units,
        "by_year": by_year
    }
