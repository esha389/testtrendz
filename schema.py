from pydantic import BaseModel
from typing import Optional




class SubjectCreate(BaseModel):
    name: str
    semester: int

class SubjectResponse(BaseModel):
    id: int
    name: str
    semester: int

    class Config:
        orm_mode = True

class QuestionPaperResponse(BaseModel):
    id: int
    subject_id: int
    year: int
    exam_type: str
    image_path: Optional[str] = None

    class Config:
        from_attributes = True