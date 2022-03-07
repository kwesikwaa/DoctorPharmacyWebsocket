from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse


app = FastAPI()

@app.websocket('/hospital')
async def connectsocket(skt: WebSocket):
    print('Connecting.....')
    await skt.accept()
    print('....connected')
    while True:
        try:
            text = await skt.receive_text()
            await skt.send_text(f'from server: {text}')
        except:
            break