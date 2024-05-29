from pydantic import BaseModel


class ExternalInfo(BaseModel):
    external_system_name: str
    external_request_id: str
