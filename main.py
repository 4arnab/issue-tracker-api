from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.issues import router as issues_router
from app.middleware.timer import timeing_middleware

app = FastAPI()

# Middlewares
app.middleware("http")(timeing_middleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins= ["http://localhost:5173", "http://localhost:5174"],
    allow_credentials=True,
    allow_methods= ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers= ["*"],
)

#wiring up routes
app.include_router(issues_router)

@app.get("/health")
def read_root():
    return {"status": "ok"}
