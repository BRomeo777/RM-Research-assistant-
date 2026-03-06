from fastapi.middleware.cors import CORSMiddleware
from config.settings import settings

def setup_cors(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # In production, replace with your frontend URL
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
