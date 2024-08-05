from sqlalchemy.orm import Session
from . import models, schemas

def create_test(db: Session, test: schemas.TestCreate):
    db_test = models.Test(**test.dict())
    db.add(db_test)
    db.commit()
    db.refresh(db_test)
    return db_test

def get_tests(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Test).offset(skip).limit(limit).all()

# Implement similar CRUD functions for Question, Answer, Result, and User.
