from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def main():
    return """
    <html>
        <head>
            <title>Docker Test</title>
        </head>
        <body>
            <h1>Hello World!</h1>
        </body>
    </html>
    """