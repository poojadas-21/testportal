from pydantic import BaseModel
from typing import List, Optional

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    role_id: int

    class Config:
        orm_mode = True

class TestBase(BaseModel):
    title: str
    description: Optional[str] = None

class TestCreate(TestBase):
    pass

class Test(TestBase):
    id: int

    class Config:
        orm_mode = True

class QuestionBase(BaseModel):
    question_text: str

class QuestionCreate(QuestionBase):
    test_id: int

class Question(QuestionBase):
    id: int

    class Config:
        orm_mode = True

class AnswerBase(BaseModel):
    answer_text: str
    is_correct: bool

class AnswerCreate(AnswerBase):
    question_id: int

class Answer(AnswerBase):
    id: int

    class Config:
        orm_mode = True

class ResultBase(BaseModel):
    score: int

class ResultCreate(ResultBase):
    user_id: int
    test_id: int

class Result(ResultBase):
    id: int

    class Config:
        orm_mode = True
