from fastapi import FastAPI
from routes import users

app = FastAPI(title="UserStore API")

app.include_router(
    users.router,
    prefix="/users",
    tags=["Users"]
)


@app.get("/")
def root():
    return {"message": "API running"}
