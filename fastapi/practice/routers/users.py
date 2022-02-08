from fastapi import APIRouter, Body, Form, status, HTTPException

from models.userModels import UserIn, UserOut, UserInDB

from tags import Tags

router = APIRouter(prefix="/user")

def password_hasher(raw_password: str):
    return 'supersecret' + raw_password

def save_user(user_in: UserIn):
    hashedPassword = password_hasher(user_in.password)
    print(hashedPassword)
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hashedPassword)
    print("save!")
    return user_in_db

# input과 output의 model이 다르도록 설정
@router.post("/login", response_model=UserOut, tags=[Tags.auth])
def login_user(user:UserIn = Body(..., embed=True)):
    user_saved = save_user(user)
    return user_saved

@router.post('/singUp', status_code=status.HTTP_201_CREATED, tags=[Tags.auth])
def sign_up(user:UserIn = Body(..., embed=True)):
    user_saved = save_user(user)
    return user_saved

@router.post('/formLogin', status_code=status.HTTP_200_OK, tags=[Tags.auth])
def form_login(username:str = Form(...), password:str = Form(...)):
    if username == " ":
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="username is empty", headers={"X-Error": "There goes my error"},)
    return {"username": username}