from urllib import response
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from model import Todo
# import uvicorn

from database import (
    fetch_one,
    fetch_all,
    create_one,
    update_one,
    del_one
)


app = FastAPI()

origins = ['https://localhost:3000']    # Здесь будет наш фронтенд ReactJS

app.add_middleware(
    CORSMiddleware, 
    allow_origins=origins, 
    allow_credentials = True, 
    allow_methods=["*"], 
    allow_headers=["*"])


@app.get('/')
async def main_menu():
    response = await fetch_all()
    return response


@app.get('/todo')
async def todo_list():
    response = await fetch_all()
    return response


@app.get('/todo{title}', response_model=Todo)        # пишем в стиле /todoTitle
async def get_todo(title: str):
    response = await fetch_one(title=title)
    if response:
        return response
    raise HTTPException(404, 'There is no notes')


@app.post('/todo', response_model=Todo)
async def create_todo(todo: Todo):
    response = await create_one(todo=todo)
    if response:
        return response
    raise HTTPException(400, 'Smth went wrong!')


@app.put('/todo{title}', response_model=Todo)
async def update_todo(title: str, desc: str):
    response = await update_one(title=title, desc=desc)
    if response:
        return response
    raise HTTPException(404, 'There is no todos')    


@app.delete('/todo{title}')
async def delete_todo(title: str):
    response = await del_one(title=title)
    if response:
        return 'Deleted'
    raise HTTPException(404, 'There is no todos')







# if __name__ == "__main__":
#     uvicorn.run(app)
#     uvicorn.run(app, host="127.0.0.1", port=8000)
#     Либо в терминале uvicorn path:app --reload
#     uvicorn path:app --host 127.0.0.1 --port 8000 --reload
