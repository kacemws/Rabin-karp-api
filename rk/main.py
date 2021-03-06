from fastapi import FastAPI
from pydantic import BaseModel
from rk.scripts import rabin_karp_matcher
from fastapi.middleware.cors import CORSMiddleware

class Message(BaseModel):
    message: str
    pattern : str


app = FastAPI()

origins = [
    "https://rabin-karp-algorithm.netlify.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post('/find')
async def findPattern(msg : Message) : 
    d = 256
    q = 3
    x = rabin_karp_matcher(msg.message, msg.pattern, d, q)
    return {'message' : x}
