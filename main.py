from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()

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

@app.get("/",response_class=HTMLResponse, include_in_schema=False)
@app.get("/posts",response_class=HTMLResponse, include_in_schema=False)

def home():
    return f"<h1>{posts[0]['title']}</h1>"

@app.get("/api/posts")

def get_posts():
    return posts