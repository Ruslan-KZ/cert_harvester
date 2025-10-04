from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.api.web import frontend
from app.router import route as auth_route



app = FastAPI()  


app.mount("/downloads", StaticFiles(directory="downloads"), name="downloads")
app.mount("/static_files", StaticFiles(directory="static_files"), name="static_files")

origins = [
"http://localhost:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],    
    allow_credentials=True,
    allow_methods=["*"],        
    allow_headers=["*"],
)   



app.include_router(frontend.router, prefix="/front",tags=["Frontend"])
app.include_router(auth_route, prefix="/api/auth", tags=["Auth"])

