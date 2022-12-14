import io
import json
from generator import gen_sql
from fastapi import FastAPI,HTTPException,Query
from fastapi.responses import StreamingResponse,FileResponse
from fastapi.staticfiles import StaticFiles


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get('/')
def root():
    return FileResponse('index.html')
    

@app.get('/gensql/{table}')
def generate_sql(table:str,qty:int,columns:str=Query(...)):
    columns = columns.strip()
    columns = [field for field in columns.split(',') if field != '']
    # ===========================
    with open('static/types.json') as file:
        available = json.load(file)
        for field in columns:
            if not field in available:
                raise HTTPException(status_code=400,detail=f"unrecognized key:'{field}'")
    # =============================
    sql = gen_sql(table,qty,columns)
    file = io.StringIO()
    file.write(sql)
    file.seek(0)
    return StreamingResponse(file)

