import logging
import os
import sys

from fastapi_pagination import add_pagination
from fastapi_sqlalchemy import DBSessionMiddleware
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import HTMLResponse

from app.admin.utils import currentTime
from app.database import init_db
from app.env import DB_URL
from mangum import Mangum

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
baseurl = os.path.dirname(os.path.abspath(__file__))
from fastapi import FastAPI, APIRouter, Depends, HTTPException
from app.routers.user import router as user_router
from app.routers.article import router as article_router
from app.routers.chatbot import router as chatbot_router
from app.test.user import router as test_router
from app.admin.pagination import router as pagination_router
from app.cloth.router import router as cloth_router

from fastapi.security import APIKeyHeader
API_TOKEN = "SECRET_API_TOKEN"
api_key_header = APIKeyHeader(name="Token")
print(f" ################ app.main Started At {currentTime()} ################# ")
router = APIRouter()
router.include_router(user_router, prefix="/users", tags=["users"])
router.include_router(article_router, prefix="/articles", tags=["articles"])
router.include_router(chatbot_router, prefix="/chatbot", tags=["chatbot"])
router.include_router(test_router, prefix="/test", tags=["test"])
router.include_router(pagination_router, prefix="/pagination", tags=["pagination"])
router.include_router(cloth_router, prefix="/cloth", tags=["cloth"])
app = FastAPI()
add_pagination(app)
origins = ["http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.router.redirect_slashes = False
app.include_router(router)
app.add_middleware(DBSessionMiddleware, db_url=DB_URL)
logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

@app.get("/protected-router")
async def protected_route(token: str = Depends(api_key_header)):
    if token != API_TOKEN:
        raise HTTPException(status_code=403)
    return {"잘못된": "경로입니다"}

@app.on_event("startup")
async def on_startup():
    await init_db()

'''
@app.get("/")
async def root():
return {"message ": " Welcome Fastapi"}
'''

@app.get("/")
async def home():
    return HTMLResponse(content=f"""
<body>
<div style="width: 400px; margin: 50 auto;">
    <h1>현재 서버 구동 중입니다.</h1>
    <h2>{currentTime()}</h2>
</div>
</body>
""")

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/no-match-token")
async def no_match_token():
    return {"message": f"토큰 유효시간이 지났습니다."}

handler = Mangum(app, lifespan="off")
