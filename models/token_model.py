from pydantic import BaseModel
from typing import Optional


class Token(BaseModel):
    access_token: str
    token_type: str

class BodyGetTokenOAuthTokenPost(BaseModel):
    grant_type: str = "password"
    username : str
    password: str
    scope: Optional[str] = None
    client_id: Optional[str] = None
    client_secret: Optional[str] = None