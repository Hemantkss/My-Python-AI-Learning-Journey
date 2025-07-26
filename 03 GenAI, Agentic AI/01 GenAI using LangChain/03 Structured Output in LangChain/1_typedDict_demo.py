from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int
    number: int
    
new_person: Person = {
    "name": "Hemant Sable",
    "age": 25,
    "number": "123"  # This will Not Throw an Error also work as int
}

print(new_person)