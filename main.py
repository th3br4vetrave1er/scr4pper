from fastapi import FastAPI

# declaring fastapi object

app = FastAPI()

# implementing testing endpoint

@app.get('/')
async def root():
    return {'message': 'Hello World'}

