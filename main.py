from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_data():
    return{"message":"hello world"}