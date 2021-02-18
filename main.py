from fastapi import FastAPI
from pydantic import BaseModel
from scripts import rabin_karp_matcher

class Message(BaseModel):
    message: str
    pattern : str


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post('/find')
async def findPattern(msg : Message) : 
    d = 256
    q = 3
    x = rabin_karp_matcher(msg.message, msg.pattern, d, q)
    return {'message' : x}
