from typing import Dict

from pydantic import BaseModel, ConfigDict


class QuotasModel(BaseModel):
    total: int
    used: int
    remaining: int


class AccountStatus(BaseModel):
    account_id: int
    quotas: Dict[str, QuotasModel]

    model_config = ConfigDict(arbitrary_types_allowed=True)
