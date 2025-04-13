import asyncio
import ssl
import websockets

async def test_websocket():
    ssl_context = ssl.create_default_context()
    uri = "wss://store.mangosand-42b1c45e.eastus.azurecontainerapps.io/ws/"
    try:
        async with websockets.connect(uri, ssl=ssl_context) as websocket:
            print("Connection established!")
            # Спробуйте отримати дані
            data = await websocket.recv()
            print("Received data:", data)
    except Exception as e:
        print("Error:", e)

asyncio.run(test_websocket())
