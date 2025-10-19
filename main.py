from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.api.router import route as main_route



app = FastAPI(title="Coursera Cert Harvester", version="1.0.0")  


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



if __name__=="__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)

