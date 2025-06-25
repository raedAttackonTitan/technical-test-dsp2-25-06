from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class BalanceType(str, Enum):
    CLBD = "CLBD"
    XPCD = "XPCD"
    VALU = "VALU"
    ITAV = "ITAV"
    PRCD = "PRCD"
    OTHR = "OTHR"

class BalanceSchema(BaseModel):
    id: Optional[str] = Field(default=None, pattern="^blnc_[a-zA-Z0-9]{24}$")
    name: str
    amount: int
    currency: str
    type: BalanceType