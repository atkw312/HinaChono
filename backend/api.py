from fastapi import FastAPI, Response
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from character import generate_chat, initialize_fastapi
from sdpipeline import generate_image
from prompt import get_gpt_prompt
from io import BytesIO
import gc
import torch

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)

p_template = ""
 
class Params(BaseModel):
    reply: str

class ImageParams(BaseModel):
    prompt: str

class LoadParams(BaseModel):
    name: str
    proj: str
    org: str
    key: str

@app.get("/")
def root():
    return {'fastapi api'}

@app.post("/onLoad/")
async def onLoad(params: LoadParams):
    global p_template
    initialize_fastapi(params.proj, params.org, params.key)
    p_template = get_gpt_prompt(params.name)
    reply = await generate_chat(prompt=p_template)
    return Response(content=reply, media_type="text/plain")

@app.post("/generate_response/")
async def get_text(params: Params):
    global p_template

    prompt = p_template + ' ' + params.reply
    reply = await generate_chat(prompt)
    return Response(content=reply, media_type="text/plain")

@app.post("/generate_image/")
async def get_image(params: ImageParams):
    prompt = params.prompt
    
    gc.collect()
    torch.cuda.empty_cache()

    image = await generate_image(prompt)

    buffer = BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)

    return StreamingResponse(buffer, media_type="image/png")
