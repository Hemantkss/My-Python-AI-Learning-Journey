from pydantic import BaseModel, EmailStr, Field
from typing import Optional

# Schema 
class Product(BaseModel):
    name: str
    price: float
    tags: list[str]
    age: Optional[int] = None
    # email: EmailStr
    cgpa: float = Field(gt=0, lt=10)

data = Product(name="iPhon", price="999", tags=["tech", "apple"], age=25, cgpa=9.5)
print(data)
print("Name: ", data.name)
print("Price: ", data.price)
print("Tags: ", data.tags)
print("Age: ", data.age)
# print("Email: ", data.email)
print("CGPA: ", data.cgpa)
print(type(data))
