from fastapi import FastAPI, Response
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from character import generate_chat
from sdpipeline import generate_image
from prompt import get_gpt_prompt
from character import set_key
from io import BytesIO
import os
import time
import base64

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)

p_template = ""
# key = ""
 
class Params(BaseModel):
    reply: str

class ImageParams(BaseModel):
    prompt: str

class LoadParams(BaseModel):
    name: str
    key: str

@app.get("/")
def root():
    return {'fastapi api'}

@app.post("/onLoad/")
async def onLoad(params: LoadParams):
    global p_template
    p_template = get_gpt_prompt(params.name)
    set_key(params.key)
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
    
    image = await generate_image(prompt)

    # timestamp = time.strftime("%Y%m%d_%H%M%S")
    # output_folder = "./testerimages"
    # image_path = os.path.join(output_folder, f"{timestamp}.png")

    buffer = BytesIO()
    # image.save(image_path)
    image.save(buffer, format="PNG")
    # imgstr = base64.b64encode(buffer.getvalue()).decode("utf-8")
    buffer.seek(0)





    imgstr = "22"

    return StreamingResponse(buffer, media_type="image/png")
