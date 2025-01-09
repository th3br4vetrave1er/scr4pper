from fastapi import FastAPI
from database import create_db_and_tables
# declaring fastapi object

app = FastAPI()

# add startup

@app.on_event('startup')
def on_startup():
    create_db_and_tables()

# implementing testing endpoint


@app.get('/')
async def root():
    return {'message': 'Hello World'}


