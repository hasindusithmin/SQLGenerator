import json
from fastapi import FastAPI,HTTPException,Query


app = FastAPI()

@app.get('/')
def root():
    raise HTTPException(status_code=200) 

@app.get('/gen')
def gen_sql(keys:str=Query(...)):
    keys = keys.strip()
    keys = [key for key in keys.split(',') if key != '']
    with open('static/types.json') as file:
        available = json.load(file)
        for key in keys:
            if not key in available:
                raise HTTPException(status_code=400,detail=f"unrecognized key:'{key}'")
    return
