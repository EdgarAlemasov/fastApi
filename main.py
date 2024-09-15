from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_table, delete_table
from router import router as tasks_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_table()
    print("clear")
    await create_table()
    print('success')
    yield
    print("stop")
 

app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)
