from pydantic import BaseModel


# 登录请求参数
class LoginRequest(BaseModel):
    username: str
    password: str
