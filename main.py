
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine
from websocket_manager import manager

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Volleyball Stats API Running"}

@app.websocket("/ws/{team_id}")
async def websocket_endpoint(websocket: WebSocket, team_id: int):
    await manager.connect(websocket, team_id)
    while True:
        data = await websocket.receive_json()
        await manager.broadcast(team_id, data)
