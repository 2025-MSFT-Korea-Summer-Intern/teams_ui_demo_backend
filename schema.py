from pydantic import BaseModel
from typing import Literal, List, Optional


class TermInfo(BaseModel):
    type: Literal["explanation"] = "explanation"
    timestamp: str
    entity: str
    domain: Optional[str] = "-"
    body: str

    class Config:
        schema_extra = {
            "example": {
                "type": "explanation",
                "timestamp": "2024-06-10T12:38:56.789Z",
                "entity": "Throughput",
                "domain": "EnterpriseIT",
                "body": "처리량은 단위 시간당 처리 가능한 데이터의 양입니다."
            }
        }
    

class TermListResponse(BaseModel):
    term_list: List[TermInfo]

    class Config:
        schema_extra = {
            "example": {
                "term_list": [
                    {
                        "type": "explanation",
                        "timestamp": "2024-06-10T12:38:56.789Z",
                        "entity": "Throughput",
                        "domain": "EnterpriseIT",
                        "body": "처리량은 단위 시간당 처리 가능한 데이터의 양입니다."
                    }
                ]
            }
        }