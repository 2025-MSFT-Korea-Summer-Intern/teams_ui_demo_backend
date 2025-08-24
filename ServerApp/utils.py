from schema import TermInfo, TermListResponse
import random

def get_dummy_history(
    meeting_id: str
) -> TermListResponse:
    
    dummy_terms = [
        TermInfo(
            id="123e4567-e89b-12d3-a456-426614174000",
            term="Latency",
            category="Metric",
            confidence=0.96,
            timestamp="2024-06-10T12:34:56.789Z",
            source_text="네트워크 지연이 커지면 사용자 경험이 나빠집니다.",
            explanation="요청과 응답 사이에 발생하는 지연 시간.",
            lang="ko"
        ),
        TermInfo(
            id="223e4567-e89b-12d3-a456-426614174001",
            term="Jitter",
            category="Metric",
            confidence=0.92,
            timestamp="2024-06-10T12:35:56.789Z",
            source_text="지터가 높으면 스트리밍 품질이 저하됩니다.",
            explanation="패킷 지연 시간이 들쭉날쭉하게 변하는 정도.",
            lang="ko"
        ),
        TermInfo(
            id="323e4567-e89b-12d3-a456-426614174002",
            term="Bandwidth",
            category="Metric",
            confidence=0.90,
            timestamp="2024-06-10T12:36:56.789Z",
            source_text="대역폭이 넓을수록 더 많은 데이터를 전송할 수 있습니다.",
            explanation="단위 시간당 전송 가능한 데이터의 양.",
            lang="ko"
        ),
        TermInfo(
            id="423e4567-e89b-12d3-a456-426614174003",
            term="Packet Loss",
            category="Metric",
            confidence=0.89,
            timestamp="2024-06-10T12:37:56.789Z",
            source_text="패킷 손실이 발생하면 데이터가 제대로 전달되지 않습니다.",
            explanation="전송 중 손실된 데이터 패킷의 비율.",
            lang="ko"
        ),
        TermInfo(
            id="523e4567-e89b-12d3-a456-426614174004",
            term="Throughput",
            category="Metric",
            confidence=0.88,
            timestamp="2024-06-10T12:38:56.789Z",
            source_text="처리량이 높을수록 시스템 성능이 좋습니다.",
            explanation="일정 시간 동안 처리할 수 있는 데이터의 양.",
            lang="ko"
        ),
        TermInfo(
            id="623e4567-e89b-12d3-a456-426614174005",
            term="QoS",
            category="Concept",
            confidence=0.87,
            timestamp="2024-06-10T12:39:56.789Z",
            source_text="QoS는 네트워크 품질을 보장하는 기술입니다.",
            explanation="서비스 품질을 보장하기 위한 네트워크 관리 기술.",
            lang="ko"
        ),
        TermInfo(
            id="723e4567-e89b-12d3-a456-426614174006",
            term="DNS",
            category="Protocol",
            confidence=0.86,
            timestamp="2024-06-10T12:40:56.789Z",
            source_text="DNS는 도메인 이름을 IP 주소로 변환합니다.",
            explanation="도메인 이름을 IP 주소로 변환하는 시스템.",
            lang="ko"
        ),
        TermInfo(
            id="823e4567-e89b-12d3-a456-426614174007",
            term="TCP",
            category="Protocol",
            confidence=0.85,
            timestamp="2024-06-10T12:41:56.789Z",
            source_text="TCP는 신뢰성 있는 데이터 전송을 제공합니다.",
            explanation="신뢰성 있는 연결 지향형 데이터 전송 프로토콜.",
            lang="ko"
        ),
        TermInfo(
            id="923e4567-e89b-12d3-a456-426614174008",
            term="UDP",
            category="Protocol",
            confidence=0.84,
            timestamp="2024-06-10T12:42:56.789Z",
            source_text="UDP는 빠른 데이터 전송에 적합합니다.",
            explanation="비연결형 데이터 전송 프로토콜.",
            lang="ko"
        ),
        TermInfo(
            id="a23e4567-e89b-12d3-a456-426614174009",
            term="Firewall",
            category="Security",
            confidence=0.83,
            timestamp="2024-06-10T12:43:56.789Z",
            source_text="방화벽은 외부 공격을 차단합니다.",
            explanation="네트워크 접근을 제어하는 보안 시스템.",
            lang="ko"
        ),
        TermInfo(
            id="b23e4567-e89b-12d3-a456-42661417400a",
            term="VPN",
            category="Security",
            confidence=0.82,
            timestamp="2024-06-10T12:44:56.789Z",
            source_text="VPN은 안전한 통신을 제공합니다.",
            explanation="가상 사설망을 통한 안전한 네트워크 연결.",
            lang="ko"
        ),
        TermInfo(
            id="c23e4567-e89b-12d3-a456-42661417400b",
            term="Proxy",
            category="Security",
            confidence=0.81,
            timestamp="2024-06-10T12:45:56.789Z",
            source_text="프록시는 사용자의 IP를 숨깁니다.",
            explanation="중계 서버를 통한 네트워크 요청 대리.",
            lang="ko"
        ),
        TermInfo(
            id="d23e4567-e89b-12d3-a456-42661417400c",
            term="Router",
            category="Device",
            confidence=0.80,
            timestamp="2024-06-10T12:46:56.789Z",
            source_text="라우터는 네트워크 트래픽을 관리합니다.",
            explanation="네트워크 간 데이터 패킷을 전달하는 장치.",
            lang="ko"
        ),
        TermInfo(
            id="e23e4567-e89b-12d3-a456-42661417400d",
            term="Switch",
            category="Device",
            confidence=0.79,
            timestamp="2024-06-10T12:47:56.789Z",
            source_text="스위치는 여러 장치를 연결합니다.",
            explanation="네트워크 내 장치 간 데이터 전송을 관리하는 장치.",
            lang="ko"
        ),
        TermInfo(
            id="f23e4567-e89b-12d3-a456-42661417400e",
            term="Hub",
            category="Device",
            confidence=0.78,
            timestamp="2024-06-10T12:48:56.789Z",
            source_text="허브는 데이터를 모든 포트로 전송합니다.",
            explanation="모든 연결된 장치로 데이터를 전송하는 네트워크 장치.",
            lang="ko"
        ),
        TermInfo(
            id="g23e4567-e89b-12d3-a456-42661417400f",
            term="IP Address",
            category="Concept",
            confidence=0.77,
            timestamp="2024-06-10T12:49:56.789Z",
            source_text="IP 주소는 네트워크 상의 장치 식별자입니다.",
            explanation="네트워크에서 장치를 식별하는 주소.",
            lang="ko"
        ),
        TermInfo(
            id="h23e4567-e89b-12d3-a456-426614174010",
            term="MAC Address",
            category="Concept",
            confidence=0.76,
            timestamp="2024-06-10T12:50:56.789Z",
            source_text="MAC 주소는 장치의 고유 식별자입니다.",
            explanation="네트워크 인터페이스의 고유 식별 번호.",
            lang="ko"
        ),
        TermInfo(
            id="i23e4567-e89b-12d3-a456-426614174011",
            term="Subnet",
            category="Concept",
            confidence=0.75,
            timestamp="2024-06-10T12:51:56.789Z",
            source_text="서브넷은 네트워크를 분할합니다.",
            explanation="네트워크를 작은 단위로 나누는 기술.",
            lang="ko"
        ),
        TermInfo(
            id="j23e4567-e89b-12d3-a456-426614174012",
            term="Gateway",
            category="Device",
            confidence=0.74,
            timestamp="2024-06-10T12:52:56.789Z",
            source_text="게이트웨이는 외부 네트워크와 연결합니다.",
            explanation="다른 네트워크로의 출입구 역할을 하는 장치.",
            lang="ko"
        ),
        TermInfo(
            id="k23e4567-e89b-12d3-a456-426614174013",
            term="DHCP",
            category="Protocol",
            confidence=0.73,
            timestamp="2024-06-10T12:53:56.789Z",
            source_text="DHCP는 IP 주소를 자동으로 할당합니다.",
            explanation="동적으로 IP 주소를 할당하는 프로토콜.",
            lang="ko"
        )
    ]
    selected_terms = random.sample(dummy_terms, 2)
    return TermListResponse(
        term_list=selected_terms
    )