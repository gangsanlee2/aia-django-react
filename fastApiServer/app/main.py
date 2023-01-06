from fastapi import FastAPI

from app.models.user import User

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.post("/security/users/login")
async def login(user: User):
    print(f"리액트에서 넘긴 정보: {user.get_email()}, {user.get_password()}")