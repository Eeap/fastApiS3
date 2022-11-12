from fastapi import FastAPI
from s3Service import s3Service
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/{name}")
async def bucket(name: str):
    s3 = s3Service()
    res = s3.makeBucket(name)
    return res
