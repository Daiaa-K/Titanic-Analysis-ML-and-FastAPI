from pydantic import BaseModel,Field,computed_field
from typing import List,Literal

class PassengerData(BaseModel):
    passenger_id:int
    age:float = Field(..., ge=0.3, le=80.0)
    fare:float = Field(..., ge=0.0, le=600.0)
    sex:Literal["male","female"]
    embarked:Literal["C","Q","S"]
    parch:int = Field(...,ge=0,le=10)
    sibsp:int = Field(...,ge=0,le=10)
    pclass:Literal[1,2,3]
    
    @computed_field
    def family_size(self) -> int:
        return self.sibsp + self.parch + 1