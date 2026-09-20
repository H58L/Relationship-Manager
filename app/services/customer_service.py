from app.schemas.customer import Customer

def get_customer(customer_id: str) -> Customer:
    return Customer(
    customer_id = customer_id,
    name = "ABC",
    industry ="Manufacturing"
)