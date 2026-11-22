from pydantic import BaseModel, ConfigDict

# 用户响应模型
class UserResponse(BaseModel):
    id: int
    name: str
    role: str
    email: str | None = None
    phone: str | None = None
    status: int

    model_config: ConfigDict = ConfigDict(from_attributes=True)

