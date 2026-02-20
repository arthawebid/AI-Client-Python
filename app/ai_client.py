import requests
import logging
from .config import Config

logger = logging.getLogger(__name__)

def ask_ai(prompt="", model="flash"):
    if not Config.AI_BASE_URL:
        return {"status": "error", "message": "AI_BASE_URL belum dikonfigurasi"}

    url = Config.AI_BASE_URL.rstrip("/") + "/api/ask"

    payload = {
        "prompt": prompt,
        "model": model
    }

    try:
        response = requests.post(
            url,
            json=payload,
            timeout=Config.AI_TIMEOUT,
            verify=Config.VERIFY_SSL
        )
    except requests.exceptions.RequestException as e:
        logger.error(f"Request Error: {str(e)}")
        return {"status": "error", "message": "Request Error"}

    if response.status_code != 200:
        logger.error(f"HTTP Error {response.status_code}: {response.text}")
        return {
            "status": "error",
            "message": f"HTTP Error ({response.status_code})"
        }

    try:
        data = response.json()
    except ValueError:
        logger.error("JSON Decode Error")
        return {"status": "error", "message": "JSON Decode Error"}

    return {
        "status": "ok",
        "agentID": data.get("agentID"),
        "agent": data.get("agent"),
        "model": data.get("model"),
        "response": data.get("response"),
        "timestamp": data.get("timestamp")
    }