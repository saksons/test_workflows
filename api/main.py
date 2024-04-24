from uvicorn import run

if __name__ == "__main__":
    run("api.api:app", host="0.0.0.0", port=50901, reload=True)