#Response Model for Prediction API
#this file defines the structure of the response returned by the server after making a prediction.

from altair import Dict
from pydantic import BaseModel, Field


class PredictionResponse(BaseModel):
    predicted_category:str=Field(...,description="The predicted insurance premium category",
                                 example="Low")
    
    confidence:float=Field(...,description="Model's confidence score for the predicted class",
                           example=0.8432)
    
    class_probabilities:dict[str,float]=Field(...,description="Probability distrubition across all possible classes",
                                              example={"Low":0.01,"Medium":0.15,"High":0.84}
                                            )
    