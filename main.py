import os
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from qna import answer_question
from explanation_module import explain_topic
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(title="EduGenie - Google Gemini Powered Learning Assistant")
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


class TextRequest(BaseModel):
    text: str


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/qa")
async def qa(payload: TextRequest):
    return {"result": answer_question(payload.text)}


@app.post("/explain")
async def explain(payload: TextRequest):
    return {"result": explain_topic(payload.text)}


@app.post("/quiz")
async def quiz(payload: TextRequest):
    return generate_quiz(payload.text)


@app.post("/summarize")
async def summarize(payload: TextRequest):
    return {"result": summarize_text(payload.text)}


@app.post("/learn/recommendations")
async def learning_recommendations(payload: TextRequest):
    return {"result": get_learning_recommendations(payload.text)}


@app.get("/health")
async def health():
    return {"status": "ok", "service": "EduGenie"}
