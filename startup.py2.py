from fastapi import FastAPI
from mysql.connector import connect 
from fastapi import Request # This line is incomplete/unnecessary for the rest of the code shown, but included from image 1
from pydantic import BaseModel
import os # Included from image 2, line 21 context
import json # Included from image 2, line 24 context

# --- Pydantic Data Model ---
class IMDBBase(BaseModel):
    imdb_id: str
    popularity: str
    director: str
    genere: str # Typo from image (should be 'genre')
    imdb_score: str
    name: str


app = FastAPI()

@app.put('/insert-data')
def insert_data(imdb_base: IMDBBase):
    print(imdb_base.dict())
    try:
        os.mkdir('TempDB')
    except Exception as ex:
        pass # Better would be to catch FileExistsError, but using 'pass' as shown in image context.
    
    with open('TempDB/imdb_database.json', mode='w') as f:
        json.dump(imdb_base.dict(), f, indent=2)
    return {'message': 'data inserted successfully'}
def insert_data_into_database(imdb_base: IMDBBase):

   @app.put('/insert-data-in-db')
   def insert