# Import libraries
import uvicorn 
from fastapi import FastAPI

#Create the app object
app = FastAPI()

@app.get('/')
def index():
    return {'message': 'Hello, World'}

# Route with a single parameter, returns the parameter within a message
#    Located at: http://0.0.0.0:8000/AnyNameHere
@app.get('/Welcome')
def get_name(name: str):
    return {'Welcome To Vajiha ML model prediction': f'{name}'}


# Run the API with uvicorn
#    Will run on http://0.0.0.0:8000
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
