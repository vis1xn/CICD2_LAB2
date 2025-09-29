from fastapi import FastAPI, HTTPException, status
from .schemas import User

users: list[User] = []
app = FastAPI()
@app.get("/hello")
def hello():
 return {"message": "Hello, World!"}

@app.get("/api/users")
def get_users():
    return users

@app.get("/api/users/{user_id}")
def get_user(user_id: int):
    for u in users:
        if u.user_id == user_id:
            return u
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

@app.post("/api/users", status_code=status.HTTP_201_CREATED)
def add_user(user: User):
    if any(u.user_id == user.user_id for u in users):
         raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="user_id already exists")
    users.append(user)
    return user

@app.put("/api/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def update_user(user_id: int):
    for u in users:
        if u.user_id == user_id:
         return {"message":"User updated"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

@app.delete("/api/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int):#
    for u in users:
        if u.user_id == user_id:
         return {"message":"204 No Content"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")


@app.get("/api/health")
def health():
    return{"status":"ok"}