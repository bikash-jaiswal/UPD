import logging

from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.post("/submit", response_class=HTMLResponse)
async def handle_form(request: Request, user_name: str = Form(...), items: list[str] = Form(...)):
    items_list = items
    logging.debug(f"The item selected are: {items_list}")
    return templates.TemplateResponse("result.html", {"request": request, "user_name": user_name, "items": items_list})
