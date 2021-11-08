# Import libraries
import uvicorn
from fastapi import FastAPI
from Spx import Spx
import numpy as np
import pickle
import pandas as pd

# Create the app object
app = FastAPI()
# Load the pickle file
pickle_in = open("classifier.pkl","rb")
clf=pickle.load(pickle_in)

@app.get('/')
def index():
    return {'message': 'Hello, World'}

# Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/{name}')
def get_name(name: str):
    return {'Welcome to the ML prediction site': f'{name}'}

# Expose the prediction functionality on FastAPI, make a prediction from the passed
#    JSON data and return the predicted Return value 
@app.post('/predict')
def predict_spx(data:Spx):
    data = data.dict()
    dp=data['dp']
    dy=data['dy']
    ep=data['ep']
    de=data['de']
    svar=data['svar']
    bm=data['bm']
    ntis=data['ntis']
    tbl=data['tbl']
    lty=data['lty']
    ltr=data['ltr']
    tms=data['tms']
    dfy=data['dfy']
    dfr=data['dfr']
    infl=data['infl']

    # Pass the feature values 
    prediction = clf.predict([[dp,dy,ep,de,svar,bm,ntis,tbl,lty,ltr,tms,dfy,dfr,infl]])
    if(prediction[0]==0):
        prediction="0"
    else:
        prediction="1"
    return {
        'prediction': prediction
    }

#  Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
    
