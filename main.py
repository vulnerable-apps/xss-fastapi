from fastapi import FastAPI, Request, Form, Depends
from fastapi.templating import Jinja2Templates
from starlette.responses import FileResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
def main_page(request: Request):
    query = request.query_params.get('query')
    if not query:
        return templates.TemplateResponse("main_page.html", {"request": request})
    else:
        message = f"Sorry, no results were found for <b>{query}</b>. <a href='?'>Try again</a>."
        return templates.TemplateResponse("results.html", {"request": request, "message": message})

@app.get("/static/{file_path}")
async def static_file(file_path: str):
    # Serve static files, update the base directory path according to your file structure
    return FileResponse(f"static/{file_path}")