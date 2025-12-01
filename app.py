from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

suffix_map = {
    "a": "알파",
    "b": "베타",
    "r": "감마",
    "d": "델타"
}

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("{page}", response_class=HTMLResponse)
async def render_page(request: Request, page: str):
    # URL에 "rara100"이 포함되어 있지 않을 경우: 404 오류 반환
    if not page.startswith("rara100"):
        raise HTTPException(status_code=404, detail="페이지를 찾을 수 없습니다.")
    
    # "+"가 포함되어 있을 경우: rara100plus.html 반환
    if "+" in page:
        suffix_for = page.split("+", 1)[-1]
        suffix_kor_parts = [suffix_map.get(ch, ch) for ch in suffix_for]
        suffix_kor = "".join(suffix_kor_parts)

        images = [
            f"https://pszhinenoljidriqjxou.supabase.co/storage/v1/object/public/rara100preview/{page}/{i}.avif"
            for i in range(1, 101)
        ]

        title = f"라라100개 미리보기 - 라라100개 플러스 {suffix_kor}"
        
        return templates.TemplateResponse(
            "rara100plus.html",
            {
                "request": request,
                "images": images,
                "title": title,
                "suffix_for": suffix_for,
                "suffix_kor": suffix_kor
            }
        )
    # "+"가 포함되어 있지 않을 경우: rara100.html 반환
    else:
        images = [
            f"https://pszhinenoljidriqjxou.supabase.co/storage/v1/object/public/rara100preview/{page}/{i}.avif"
            for i in range(1, 101)
        ]
    
        title = "라라100개 미리보기 - 라라100개"

        return templates.TemplateResponse(
            "rara100.html",
            {
                "request": request,
                "images": images,
                "title": title
            }
        )