# Truzz Blogg - Youtube link: https://youtu.be/q-N6IcgCqCE
# Speech recognition in Python ::: How to convert an Audio File to Text

from gtts import gTTS
from fastapi import FastAPI, HTTPException,Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.responses import StreamingResponse




app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.get("/")
def home():
    return {"<b> It's works </b>"}


@app.get("/audio/", status_code=200)
def audio(context: str,lang: str):
    try:
          
        tts = gTTS(text=context, lang=lang)
        filewav = "hello.wav"
        tts.save(filewav)
        audio_file = open(filewav, mode="rb")

    except Exception as e:
        error = str(e)
        raise HTTPException(status_code=500, detail=error)
    
    return StreamingResponse(audio_file, media_type="audio/wav")
