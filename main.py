from fastapi import FastAPI,Request, HTTPException,status
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

@app.get("/", include_in_schema=False,name="home")
@app.get("/posts", include_in_schema=False,name="posta")

def home(request:Request):
    return templates.TemplateResponse(request,"home.html", {"posts":posts, "title": "Home"},)

@app.get("/api/posts")

def get_posts():
    return posts



@app.get("/api/posts/{post_id}")
def get_post(post_id: int):
    for post in posts:
        if post.get("id") == post_id:
            return post
    raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="post not found")
