from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class AccountType(str, Enum):
    CACC = "CACC"
    CARD = "CARD"


class AccountUsage(str, Enum):
    PRIV = "PRIV"
    ORGA = "ORGA"


class AccountSchema(BaseModel):
    id: Optional[str] =  Field(default=None, pattern="^acct_[a-zA-Z0-9]{24}$")
    type: AccountType
    usage: AccountUsage
    iban: str
    name: str
    currency: str
