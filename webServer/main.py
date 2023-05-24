import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return ['a','b','c']

@app.get('/contact', response_class = HTMLResponse)
def get_list():
   # return {'name': 'Ejemplo'}
    return """
        <h1> Holaaaaa </h1>
        <p> parrafo <p>  
    """

def run():
    store.get_categories()

if __name__ == '__main__':
    run()