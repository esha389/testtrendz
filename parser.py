import re

def parse_question_paper(text: str, subject: str, year: int):
    questions = []
    current_unit = None

    lines = [line.strip() for line in text.split("\n") if line.strip()]

    for line in lines:
        # Detect Unit
        unit_match = re.match(r"Unit\s*[-–]\s*(\w+)", line, re.IGNORECASE)
        if unit_match:
            current_unit = unit_match.group(1)
            continue

        # Detect questions like: 1. a) Question text
        q_match = re.match(r"(\d+)\.\s*[a-z]\)\s*(.*)", line, re.IGNORECASE)
        if q_match and current_unit:
            questions.append({
                "unit": current_unit,
                "question_no": q_match.group(1),
                "question_text": q_match.group(2),
                "marks": 2,  # default for Part A
                "subject": subject,
                "year": year
            })

    return questions
