# app/schemas.py
from pydantic import BaseModel, EmailStr, constr, conint, constr
class User(BaseModel):
 user_id: int
 student_id: constr(pattern='^S\d{7}$')
 name: constr(min_length=2, max_length=50)
 email: EmailStr
 age: conint(gt=18)