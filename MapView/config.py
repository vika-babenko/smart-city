import os

STORE_HOST = os.environ.get("STORE_HOST") or "store.mangosand-42b1c45e.eastus.azurecontainerapps.io"
STORE_PORT = os.environ.get("STORE_PORT") or "443"

HUB_HOST = os.environ.get("HUB_HOST") or "hub.mangosand-42b1c45e.eastus.azurecontainerapps.io"
HUB_PORT = os.environ.get("HUB_PORT") or "443"
if STORE_PORT == "443":
    WS_SCHEME = "wss"
else:
    WS_SCHEME = "ws"
WEBSOCKET_URL = f"{WS_SCHEME}://{STORE_HOST}/ws/"
