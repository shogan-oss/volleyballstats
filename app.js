
const teamId = 1;
const ws = new WebSocket(`ws://localhost:8000/ws/${teamId}`);

function sendStat(stat) {
    ws.send(JSON.stringify({ stat: stat }));
}
