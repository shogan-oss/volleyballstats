
from fastapi import WebSocket

class Manager:
    def __init__(self):
        self.connections = {}

    async def connect(self, websocket: WebSocket, team_id: int):
        await websocket.accept()
        if team_id not in self.connections:
            self.connections[team_id] = []
        self.connections[team_id].append(websocket)

    async def broadcast(self, team_id: int, message: dict):
        for ws in self.connections.get(team_id, []):
            await ws.send_json(message)

manager = Manager()
