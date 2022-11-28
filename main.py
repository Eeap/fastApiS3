from fastapi import FastAPI, UploadFile, File
from s3Service import s3service
app = FastAPI()


@app.get("/{name}")
async def bucket(name: str):
    s3 = s3service()
    res = s3.makeBucket(name)
    return res
@app.post("/upload")
async def put_images(file: UploadFile = File(None)):
    s3 = s3service()
    res = s3.upload_file(file)
    return res