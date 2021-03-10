import fastapi
import uvicorn

app = fastapi.FastAPI()


@app.get('/')
def index():
    content = """
    
    <h1> Fast API with HTML response </h1>
    
    <div> This page is in HTML </div>
    
    """
    response = fastapi.responses.HTMLResponse(content)
    return response
        # initial JSON return:
    # 'message': "Hello world"


if __name__ == '__main__':
    uvicorn.run(app)
