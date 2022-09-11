import motor.motor_asyncio

from model import Todo


client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')
database = client.TodoList
collection = database.todo


async def fetch_one(title: str):
    note = await collection.find_one({"title": title})
    return note


async def fetch_all():
    notes = []
    base = collection.find({})
    async for document in base:
        notes.append(Todo(**document))
    return notes


async def create_one(todo):
    await collection.insert_one(todo.dict())
    return todo


async def update_one(title, desc):
    await collection.update_one({"title": title}, {"$set": {"description": desc}})
    document = await collection.find_one({"title": title})
    return document


async def del_one(title):
    await collection.delete_one({"title": title})
    return True
    