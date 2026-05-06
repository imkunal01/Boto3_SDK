from fastapi import FastAPI

# Initialize the FastAPI application
app = FastAPI(
    title="CloudTasker",
    description="A Dockerized task management API",
    version="1.0.0"
)

# Health Check Route
@app.get("/")
async def health_check():
    """
    Basic health check endpoint to verify the server is running.
    """
    return {
        "status": "success",
        "message": "CloudTasker API is up and running!"
    }