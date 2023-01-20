from faker import Faker
from fastapi import Depends, APIRouter
from starlette.responses import JSONResponse

from app.database import get_db
from sqlalchemy.orm import Session
from app.cruds.user import UserCrud
router = APIRouter()

from app.schemas.user import UserDTO
from app.admin.utils import between_random_date


@router.get("/page/{request_page}")
def pagination(request_page: int, db: Session = Depends(get_db)):
    row_cnt = UserCrud(db).count_all_users()
    page_size = 10
    t1 = row_cnt // page_size   # 몫
    t2 = row_cnt % page_size    # 나머지
    page_cnt = t1 if (t2 == 0) else t1 + 1
    block_size = 10
    t1 = page_cnt // block_size
    t2 = page_cnt % block_size
    block_cnt = t1 if (t2 == 0) else t1 + 1
    response_page = request_page -1
    row_start = page_size * response_page
    row_end = (row_cnt - 1) if page_cnt == response_page + 1 else row_start + page_size -1
    block_now = response_page // block_size
    page_start = block_now * block_size
    page_end = page_cnt - 1 if (block_cnt-1) == block_now else page_start + block_size - 1

    print("### 테스트 ### ")
    print(f"row_start ={row_start}")
    print(f"row_end ={row_end}")
    print(f"page_start ={page_start}")
    print(f"page_end ={page_end}")
    print(f" count is {row_cnt}")

    return JSONResponse(status_code=200,
                        content=dict(msg=row_cnt))


@router.get("/many")
def insert_many(db: Session = Depends(get_db)):
    [UserCrud(db).add_user(create_faker_user()) for i in range(100)]


def create_faker_user():
    faker = Faker('ko_KR')
    return UserDTO(user_email=faker.email(),
                   password="12qw",
                   user_name=faker.name(),
                   birth=between_random_date(),
                   address=faker.city())
