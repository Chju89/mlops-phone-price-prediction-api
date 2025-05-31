from pydantic import BaseModel, Field

class PhoneData(BaseModel):
    Company_Name: str = Field(alias="Company Name")
    Model_Name: str = Field(alias="Model Name")
    Processor: str
    Launched_Year: int = Field(alias="Launched Year")
    Mobile_Weight: str = Field(alias="Mobile Weight")
    RAM: str
    Front_Camera: str = Field(alias="Front Camera")
    Back_Camera: str = Field(alias="Back Camera")
    Battery_Capacity: str = Field(alias="Battery Capacity")
    Screen_Size: str = Field(alias="Screen Size")
    Country: str

    model_config = {
        "populate_by_name": True,
        "json_schema_extra": {
            "example": {
                "Company Name": "Samsung",
                "Model Name": "Galaxy S21 5G 128GB",
                "Processor": "Qualcomm Snapdragon 888",
                "Launched Year": 2021,
                "Mobile Weight": "169g",
                "RAM": "8GB",
                "Front Camera": "10MP",
                "Back Camera": "12MP+64MP+12MP",
                "Battery Capacity": "4000mAh",
                "Screen Size": "6.2inches",
                "Country": "USA"
            }
        }
    }

