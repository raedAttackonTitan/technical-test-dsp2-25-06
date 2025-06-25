from typing import Literal

from pydantic import BaseModel, Field
from datetime import date
from enum import Enum

class UserPrefix(str, Enum):
    DOCT = "DOCT"
    MADM = "MADM"
    MISS = "MISS"
    MIST = "MIST"

class UserIdentitySchema(BaseModel):
    id: str = Field(default=None, pattern="^user_[a-zA-Z0-9]{24}$")
    prefix: UserPrefix
    first_name: str
    last_name: str
    date_of_birth: date
