from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get('/api/helloWorld')
def heelo_world():
    '''
    Endpoint com hello world
    '''

    return {'Hello':'World'}