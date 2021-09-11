from fastapi import FastAPI

app = FastAPI()


def get_response(msg):
    return dict(response=msg)


@app.get("/")
def get_root():
    return get_response("Hello there!")


@app.get("/status")
def get_status():
    return get_response("OK")


@app.post("/echo")
def post_echo(body: dict):
    return get_response(body)
