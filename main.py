from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.router import route as auth_route
from fastapi.staticfiles import StaticFiles


app = FastAPI()  
  
app.add_middleware(CORSMiddleware,
    allow_origins=["*"],    
    allow_credentials=True,
    allow_methods=["*"],        
    allow_headers=["*"],
)   
app.include_router(auth_route, prefix="/api")
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/", StaticFiles(directory="static", html=True), name="static")


