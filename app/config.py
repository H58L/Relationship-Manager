from dotenv import load_dotenv
import os

load_dotenv()

swagger_api_token = os.getenv("SWAGGER_API_TOKEN")

if not swagger_api_token:
    raise RuntimeError("SWAGGER_API_TOKEN is not configured in .env file")