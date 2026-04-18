from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles



app = FastAPI()

app.mount("/static",StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

posts: list[dict] = [
    {
        "id":1,
        "author": "mahesh yadav",
        "title": "fastapi is awesome",
        "content": "this is frame is really easy to use",
        "date_posted": "April 18, 2026"

    
    },
    {
        "id":2,
        "author": "john don",
        "title": "python is a great web developent ",
        "content": "this is frame is really easy to use , easy to fastapi",
        "date_posted": "April 19, 2026"
    }
]

@app.get("/", include_in_schema=False)
@app.get("/posts", include_in_schema=False)

def home(request:Request):
    return templates.TemplateResponse(request,"home.html", {"posts":posts, "title": "Home"},)

@app.get("/api/posts")

def get_posts():
    return posts