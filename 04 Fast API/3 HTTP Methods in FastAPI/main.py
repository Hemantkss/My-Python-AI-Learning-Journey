from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional
import json

# Create the FastAPI app
app = FastAPI()

# Schema using Pydantic
class Patient(BaseModel):
    id: Annotated[str, Field(..., description="The unique ID of the patient", example="P001")]
    name: Annotated[str, Field(..., description="The name of the patient", example="Hemant Sabale")]
    city: Annotated[str, Field(..., description="The city where the patient resides", example="Pune")]
    age: Annotated[int, Field(..., description="The age of the patient", gt=0, lt=110)]
    gender: Annotated[Literal["male", "female", "other"], Field(..., description="The gender of the patient", example="male")]
    height: Annotated[float, Field(..., description="The height of the patient in meters", example=1.755)]
    weight: Annotated[float, Field(..., description="The weight of the patient in kg", example=70.0)]
    
    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight / (self.height ** 2), 2)
        return bmi
    
    @computed_field
    @property
    def verdict(self)-> str:
        if self.bmi < 19:
            return "UnderWeight"
        elif 19 <= self.bmi < 25:
            return "Normal"
        elif 25 <= self.bmi < 30:
            return "Overweight"
        else:
            return "Obese"


# Update Patient Information
class PatientUpdate(BaseModel):
    name: Annotated[Optional[str], Field(default=None)]
    city: Annotated[Optional[str], Field(default=None)]
    age: Annotated[Optional[int], Field(default=None, gt=0)]
    gender: Annotated[Optional[Literal["male", "female", "other"]], Field(default=None)]
    height: Annotated[Optional[float], Field(default=None)]
    weight: Annotated[Optional[float], Field(default=None)]


# Load patient data
def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
        
    return data

@app.get("/")
def home():
    return {"message": "Patients Management System API"}

@app.get("/about")
def about():
    return {"message": " A Functional API to manage patient data."}

# View all patients
@app.get("/view")
def view():
    data = load_data()
    return data


# Get a specific patient
@app.get("/patient/{patient_id}")
def get_patient(patient_id: str = Path(..., description="The ID of the patient to retrieve", example="P001")):
    data = load_data()
    
    if patient_id in data:
        return data[patient_id]
    else:
        raise HTTPException(status_code=404, detail="Patient not found")

# Sort patients
@app.get("/sort")
def sort_patients(sort_by: str = Query(..., description="The field to sort by Height, Weight, BMI, Age,", example="Xyz"), order: str = Query("asc", description="The order to sort by: asc or desc", example="asc")):
    
    valid_fields = ["height", "weight", "bmi", "age"]

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f"Invalid field Selected by {valid_fields}")
    
    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="Order must be 'asc' or 'desc'")
    
    data = load_data()

    sort_order = True if order == 'desc' else False
    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)

    return sorted_data

# Save data
def save_data(data):
    with open('patients.json', 'w') as f:
        json.dump(data, f)


# Create a new database entry using POST Request
@app.post("/create")
def create_patient(patient: Patient):
    # Load Existing DataBase
    data = load_data()
    
    # Check if the patient already exists
    if patient.id in data:
        raise HTTPException(status_code=400, detail="Patient with this ID already exists")
    
    # new patient add to database
    data[patient.id] = patient.model_dump(exclude=['id'])
    
    # Save the updated data back to the json file
    save_data(data)
    
    return JSONResponse(status_code=201, content={"message": "Patient created successfully"})


# Update an existing patient
@app.put('/edit/{patient_id}')
def update_patient(patient_id: str, patient_update: PatientUpdate):
    # Load existing data
    data = load_data()

    # Check if the patient exists
    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")

    # Update patient information
    existing_patient_info = data[patient_id]

    updated_patient_info = patient_update.model_dump(exclude_unset=True)
    
    for key, value in updated_patient_info.items():
        existing_patient_info[key] = value

    # Create a new Pydantic object
    existing_patient_info['id'] = patient_id
    patient_pydantic_object = Patient(**existing_patient_info) 
    existing_patient_info = patient_pydantic_object.model_dump(exclude='id')
           
    # Save the updated data back to the json file
    data[patient_id] = existing_patient_info
    save_data(data)
    
    return JSONResponse(status_code=200, content={"message": "Patient updated successfully"})


# Delete 
@app.delete('/delete/{patient_id}')
def delete_patient(patient_id: str):
    # Load existing data
    data = load_data()

    # Check if the patient exists
    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")

    # Delete the patient
    del data[patient_id]
    save_data(data)

    return JSONResponse(status_code=200, content={"message": "Patient deleted successfully"})
