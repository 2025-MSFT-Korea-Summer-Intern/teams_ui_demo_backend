from schema import TermInfo, TermListResponse
import random

def get_dummy_history(
    meeting_id: str
) -> TermListResponse:
    
    dummy_terms = [
        TermInfo(
            timestamp="2024-06-10T12:34:56.789Z",
            entity="Latency",
            domain="Metric",
            body="요청과 응답 사이에 발생하는 지연 시간입니다."
        ),
        TermInfo(
            timestamp="2024-06-10T12:35:56.789Z",
            entity="Jitter",
            domain="Metric",
            body="패킷 지연 시간이 들쭉날쭉하게 변하는 정도를 말합니다."
        ),
        TermInfo(
            timestamp="2024-06-10T12:36:56.789Z",
            entity="Bandwidth",
            domain="Metric",
            body="단위 시간당 전송 가능한 데이터의 양입니다."
        ),
        TermInfo(
            timestamp="2024-06-10T12:37:56.789Z",
            entity="Packet Loss",
            domain="Metric",
            body="전송 중 손실된 데이터 패킷의 비율."
        )
    ]
    selected_terms = random.sample(dummy_terms, 2)
    return TermListResponse(
        term_list=selected_terms
    )