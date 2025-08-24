# 테스트용 더미 데이터 - 실제에서는 필요 x
import time, uuid
from datetime import datetime
import asyncio
import websockets
import json

def now_iso():
    return datetime.now().isoformat(timespec="seconds").replace("+00:00", "Z")

async def test_websocket():
    uri = "ws://localhost:8080/meeting/test_meeting_123/terms"
    # Example: Add headers if your server requires authentication (e.g., token)
    headers = {
        # "Authorization": "Bearer YOUR_TOKEN_HERE"
    }
    async with websockets.connect(
        uri, extra_headers=headers, timeout=60
    ) as websocket:
        while True:
            response = await websocket.recv()
            print("Received:", response)

if __name__ == "__main__":
    asyncio.run(test_websocket())