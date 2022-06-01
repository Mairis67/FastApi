from fastapi import FastAPI
from . import models
from .database import engine
from .routes import blog, user

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(blog.router)
app.include_router(user.router)
