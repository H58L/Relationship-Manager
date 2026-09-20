from fastapi import FastAPI,Depends,HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.config import swagger_api_token
from app.schemas.customer import Customer
from app.services.customer_service import get_customer

security = HTTPBearer()
app_rm = FastAPI()


def verify_token(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    if credentials.credentials != swagger_api_token:
        raise HTTPException(status_code=401, detail="Invalid token")

    return credentials.credentials

@app_rm.get("/")
def root():
    return {"message": "Agentic RM API is running"}

@app_rm.get("/customers/{customer_id}",
            response_model=Customer,
            dependencies=[Depends(verify_token)]
            )
def customer(customer_id: str):
    return get_customer(customer_id)