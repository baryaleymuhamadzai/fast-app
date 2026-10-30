from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

HTML = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello FastAPI</title>
    <style>
        body {
            margin: 0;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: sans-serif;
        }
    </style>
</head>
<body>
    <h1>Hello World from FastAPI</h1>
</body>
</html>
"""


@app.get("/", response_class=HTMLResponse)
def read_root():
    return HTML
