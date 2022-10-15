import io
import json
from generator import gen_sql
from fastapi import FastAPI,HTTPException,Query
from fastapi.responses import StreamingResponse


app = FastAPI()

@app.get('/')
def root():
    raise HTTPException(status_code=200) 

@app.get('/gensql/{table}/{qty}')
def generate_sql(table:str,qty:int,fields:str=Query(...)):
    fields = fields.strip()
    fields = [field for field in fields.split(',') if field != '']
    # ===========================
    with open('static/types.json') as file:
        available = json.load(file)
        for field in fields:
            if not field in available:
                raise HTTPException(status_code=400,detail=f"unrecognized key:'{field}'")
    # =============================
    sql = gen_sql(table,qty,fields)
    file = io.StringIO()
    file.write(sql)
    file.seek(0)
    return StreamingResponse(file)

