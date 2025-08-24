from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from fastapi import APIRouter, APIRouter, Depends
from fastapi.responses import JSONResponse

import asyncio
from utils import get_dummy_history

router = APIRouter()
CLIENTS = set()

@router.websocket(
    path="/meeting/{meeting_id}/terms"
)
async def websocket_endpoint(ws: WebSocket, meeting_id: str):
    await ws.accept()
    CLIENTS.add(ws)
    try:
        count = 0
        while count < 3:
            obj = get_dummy_history(meeting_id)
            await ws.send_text(
            obj.model_dump_json()
            )
            await asyncio.sleep(3)
            count += 1
        await ws.close()
            
    except WebSocketDisconnect:
        print(f"WebSocket disconnected: {meeting_id}")
    except Exception as e:
        print(f"Unexpected error in websocket_endpoint (meeting_id={meeting_id}): {e}")
    finally:
        CLIENTS.discard(ws)