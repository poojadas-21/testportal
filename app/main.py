from fastapi import FastAPI
from app import auth, crud, models, schemas, database

app = FastAPI()

# Create the database tables
database.Base.metadata.create_all(bind=database.engine)

# Include the routers
app.include_router(auth.router)
#app.include_router(crud.router,prefix="/db")
