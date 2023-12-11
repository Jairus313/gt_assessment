from pydantic import BaseModel

class login_cred(BaseModel):
    username: str
    password: str