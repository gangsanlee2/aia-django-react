from fastapi import APIRouter
from starlette.responses import HTMLResponse

router = APIRouter()

@router.get("/users/login")
async def login():
    return HTMLResponse(content="""
    <form action="http://localhost:8000/users/login" method="post" style="width: 300px; margin: 50 auto;">
    <div class="container">
      <label for="uname"><b>Username</b></label>
      <input type="text" placeholder="Enter Username" name="uname" required>
        <br/>
      <label for="psw"><b>Password</b></label>
      <input type="password" placeholder="Enter Password" name="psw" required>
      <br/>
      <button type="submit">Login</button>      
    </div>    
    </form>
    """)