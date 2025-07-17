import os
from typing import Iterable, Dict

import requests

INTERCOM_BASE_URL = "https://api.intercom.io"


def _get_headers() -> Dict[str, str]:
    token = os.getenv("INTERCOM_TOKEN")
    if not token:
        raise EnvironmentError("INTERCOM_TOKEN environment variable not set")
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }


def send_new_chat(chat_data: Dict) -> Dict:
    """Send a chat message to Intercom as a conversation."""
    url = f"{INTERCOM_BASE_URL}/conversations"
    payload = {
        "from": {
            "type": chat_data.get("from_type", "user"),
            "id": chat_data.get("user_id"),
        },
        "body": chat_data.get("body"),
    }
    response = requests.post(url, json=payload, headers=_get_headers())
    response.raise_for_status()
    return response.json()


def _retrieve_chats_from_novatalks() -> Iterable[Dict]:
    """Placeholder for retrieving chats from NovaTalks."""
    # In a real implementation this would query the NovaTalks API.
    return []


def sync_existing_chats() -> None:
    """Retrieve chats from NovaTalks and send them to Intercom."""
    chats = _retrieve_chats_from_novatalks()
    for chat in chats:
        send_new_chat(chat)


try:
    from fastapi import FastAPI, HTTPException
    from pydantic import BaseModel

    app = FastAPI()

    class Chat(BaseModel):
        body: str
        user_id: str | None = None
        from_type: str | None = "user"

    @app.post("/nova_intercom/chats")
    def receive_chat(chat: Chat):
        try:
            result = send_new_chat(chat.model_dump())
            return {"id": result.get("id")}
        except Exception as exc:
            raise HTTPException(status_code=400, detail=str(exc))
except Exception:
    # FastAPI is optional; if not installed this module still works without the HTTP API.
    app = None
