from pydantic import BaseModel, Field, EmailStr, constr


class UserSchema(BaseModel):
    """
    Модель данных пользователя.
    Используется в ответах API.
    """
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserRequestSchema(BaseModel):
    """
    Модель запроса на создание пользователя.
    Используется для отправки данных в POST /api/v1/users.
    """
    email: EmailStr
    password: constr(min_length=1)
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserResponseSchema(BaseModel):
    """
    Модель ответа при успешном создании пользователя.
    """
    user: UserSchema
