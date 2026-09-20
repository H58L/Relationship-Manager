from fastapi import FastAPI,Depends,HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.schemas.customer import Customer

security = HTTPBearer()
app_rm = FastAPI()

def verify_token(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    if credentials.credentials != "lisa":
        raise HTTPException(status_code=401, detail="Invalid token")

    return credentials.credentials

@app_rm.get("/")
def root():
    return {"message": "Agentic RM API is running"}

@app_rm.get("/customers/{customer_id}",
            response_model=Customer,
            dependencies=[Depends(verify_token)]
            )
def get_customer(customer_id: str):
    return Customer(
        customer_id=customer_id,
        name="Blah blah",
        industry="bleh bleh",
        )