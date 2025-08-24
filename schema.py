from pydantic import BaseModel
from typing import Literal
from typing import List


class TermInfo(BaseModel):
    id: str
    term: str
    category: str
    confidence: float
    timestamp: str
    source_text: str
    explanation: str
    lang: Literal["ko", "en"]

    class Config:
        schema_extra = {
            "example": {
                "id": "123e4567-e89b-12d3-a456-426614174000",
                "term": "Latency",
                "category": "Metric",
                "confidence": 0.96,
                "timestamp": "2024-06-10T12:34:56.789Z",
                "source_text": "네트워크 지연이 커지면 사용자 경험이 나빠집니다.",
                "explanation": "요청과 응답 사이에 발생하는 지연 시간.",
                "lang": "ko"
            }
        }
    

class TermListResponse(BaseModel):
    term_list: List[TermInfo]

    class Config:
        schema_extra = {
            "example": {
                "term_list": [
                    {
                        "id": "123e4567-e89b-12d3-a456-426614174000",
                        "term": "Latency",
                        "category": "Metric",
                        "confidence": 0.96,
                        "timestamp": "2024-06-10T12:34:56.789Z",
                        "source_text": "네트워크 지연이 커지면 사용자 경험이 나빠집니다.",
                        "explanation": "요청과 응답 사이에 발생하는 지연 시간.",
                        "lang": "ko"
                    },
                    {
                        "id": "223e4567-e89b-12d3-a456-426614174001",
                        "term": "Jitter",
                        "category": "Metric",
                        "confidence": 0.92,
                        "timestamp": "2024-06-10T12:35:56.789Z",
                        "source_text": "지터가 높으면 스트리밍 품질이 저하됩니다.",
                        "explanation": "패킷 지연 시간이 들쭉날쭉하게 변하는 정도.",
                        "lang": "ko"
                    }
                ]
            }
        }