from datetime import datetime

from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional


class TransactionCreditDebitIndicator(str, Enum):
    CRDT = "CRDT"
    DBIT = "DBIT"


class TransactionStatus(str, Enum):
    BOOK = "BOOK"
    PDNG = "PDNG"
    FUTR = "FUTR"
    INFO = "INFO"


class TransactionSchema(BaseModel):
    id: Optional[str] = Field(default=None, pattern="^tran_[a-zA-Z0-9]{24}$")
    label: str
    amount: int
    crdt_dbit_indicator: TransactionCreditDebitIndicator
    status: TransactionStatus
    currency: Optional[str]
    date_operation: datetime
    date_processed: Optional[datetime]
