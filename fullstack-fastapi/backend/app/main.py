from fastapi import FastAPI, WebSocket, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .database import Base, engine
from .routers import doctor, patient, appointment, upload

app = FastAPI()

# ✅ CORS (required for React frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Create database tables
Base.metadata.create_all(bind=engine)

# ✅ Include routers
app.include_router(doctor.router, prefix="/doctors", tags=["Doctors"])
app.include_router(patient.router, prefix="/patients", tags=["Patients"])
app.include_router(appointment.router, prefix="/appointment", tags=["Appointment"])
app.include_router(upload.router, prefix="/upload", tags=["Upload"])

# ✅ LOGIN API
@app.post("/login")
def login(data: dict):
    if data["username"] == "admin" and data["password"] == "123":
        return {"token": "dummy-token"}
    raise HTTPException(status_code=401, detail="Invalid credentials")

# ✅ WebSocket connections
connections = []

@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    connections.append(ws)
    try:
        while True:
            data = await ws.receive_text()
            await ws.send_text(f"Echo: {data}")
    except:
        connections.remove(ws)

# ✅ Notify all connected clients
@app.post("/notify")
async def notify():
    for conn in connections:
        await conn.send_text("New Appointment!")
    return {"message": "Notification sent"}

# ✅ Root API
@app.get("/")
def home():
    return {"message": "API Running"}