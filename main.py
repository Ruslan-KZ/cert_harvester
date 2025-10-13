from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.router import route as main_route

app = FastAPI()  


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

app.include_router(main_route,prefix="/api")
