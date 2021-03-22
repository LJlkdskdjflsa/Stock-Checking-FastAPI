from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def dashboard():
    return {"message": "Hello World"}