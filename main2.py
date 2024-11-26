from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List


app = FastAPI()


users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get('/users')
async def one() -> List[User]:
    return users


@app.post('/user/{username}/{age}')
async def two(username: str, age: int) -> User:
    new_id = (users[-1].id + 1) if users else 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put('/user/{user_id}/{username}/{age}')
async def three(user_id: int, username: str, age: int) -> User:
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail='Задача не найдена')


@app.delete('/user/{user_id}')
async def four(user_id: int) -> User:
    for index, user in enumerate(users):
        if user.id == user_id:
            deleted_user = users.pop(index)
            return deleted_user
    raise HTTPException(status_code=404, detail='Задача не найдена')