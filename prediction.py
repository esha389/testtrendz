# app/prediction.py
from sqlalchemy.orm import Session
from app.models import QuestionTopic, Question, QuestionPaper

def predict_topics(db: Session, subject_id: int, top_n: int = 5):
    rows = (
        db.query(
            QuestionTopic.topic,
            QuestionPaper.year
        )
        .join(Question, Question.id == QuestionTopic.question_id)
        .join(QuestionPaper, QuestionPaper.id == Question.paper_id)
        .filter(QuestionPaper.subject_id == subject_id)
        .all()
    )

    if not rows:
        return []

    current_year = max(y for _, y in rows)

    score = {}

    for topic, year in rows:
        score.setdefault(topic, 0)
        score[topic] += 1

        if year >= current_year - 1:
            score[topic] += 2

    return sorted(
        score.items(),
        key=lambda x: x[1],
        reverse=True
    )[:top_n]
