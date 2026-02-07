from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.database import Base


class Subject(Base):
    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True, nullable=False)
    semester = Column(Integer, nullable=False)


class QuestionPaper(Base):
    __tablename__ = "question_papers"

    id = Column(Integer, primary_key=True)
    subject_id = Column(Integer, ForeignKey("subjects.id"))
    year = Column(Integer, nullable=False)
    exam_type = Column(String, nullable=False)
    image_path = Column(String, nullable=False)

    subject = relationship("Subject", backref="papers")
    questions = relationship(
        "Question",
        backref="paper",
        cascade="all, delete-orphan"
    )


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True)
    paper_id = Column(Integer, ForeignKey("question_papers.id"))
    unit = Column(String, index=True)
    question_text = Column(Text, nullable=False)
    marks = Column(Integer)

    topics = relationship(
        "QuestionTopic",
        back_populates="question",
        cascade="all, delete-orphan"
    )


class QuestionTopic(Base):
    __tablename__ = "question_topics"

    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer, ForeignKey("questions.id", ondelete="CASCADE"))
    topic = Column(String, index=True, nullable=False)

    question = relationship("Question", back_populates="topics")
