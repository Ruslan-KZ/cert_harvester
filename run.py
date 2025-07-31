import uvicorn


if __name__ == "__main__":
    uvicorn.run("cert_harvester:app", host="localhost", port=8000, reload=True)