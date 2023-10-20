from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Annotated

import requests

import models
from models import Questions
from database import Base, engine, SessionLocal

from datetime import datetime

from sqlalchemy.orm.exc import NoResultFound

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

class Question_Request(BaseModel):
    questions_num: int


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/questions')
def get_questions(questions_num: Question_Request, db=Depends(get_db)):
    for _ in range(questions_num.questions_num):
        try:
            response = requests.get(f'https://jservice.io/api/random?count={questions_num.questions_num}')
            question_data = response.json()
            for i in question_data:
                question_id = i['id']

                question_text = i['question']
                answer_text = i['answer']
                created_at = datetime.strptime(i["created_at"], "%Y-%m-%dT%H:%M:%S.%fZ")

                try:
                    db.query(Questions).filter(Questions.id == question_id).one()
                    continue
                except NoResultFound:
                    pass

                quest_n = Questions(
                    id=question_id,
                    question=question_text,
                    answer=answer_text,
                    created_at=created_at
                )
                db.add(quest_n)
                db.commit()
                db.refresh(quest_n)

            return quest_n

        except(KeyError, IndexError):
            raise HTTPException(status_code=500, detail='Failed to fetch question data')

    raise HTTPException(status_code=404, detail='No questions found')



@app.get("/get_question/{question_id}")
def get_quest(question_id: int, db=Depends(get_db)):
    try:
        ques_tion = db.query(Questions).filter(Questions.id == question_id).one()
        return ques_tion
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Question not found")