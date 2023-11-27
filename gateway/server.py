import uvicorn, os, random, logging, string, time
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from routers import auth, todo
from gunicorn.app.base import BaseApplication
from typing import Any, Callable, Dict
from fastapi_auth_middleware.middleware import AuthMiddleware, AuthenticationError
from auth.client import AuthClient

# setup loggers
logging.basicConfig(format="%(asctime)s %(levelname)s:%(message)s", level=logging.DEBUG)

# get root logger
logger = logging.getLogger(__name__)


async def verify_authorization_header(auth_header: str):
    auth_client = AuthClient()
    token = auth_header["Authorization"].split(" ")[1]
    user = auth_client.validate_token(token)
    return [], user


def authentication_error_response(request: Request, error: AuthenticationError):
    logger.debug(request.headers)
    logger.error(error)
    return JSONResponse(
        {"success": False, "message": "Authentication error"}, status_code=401
    )


exclude_route = ["/auth/v1/register", "/auth/v1/login"]

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    AuthMiddleware,
    verify_header=verify_authorization_header,
    auth_error_handler=authentication_error_response,
    excluded_urls=exclude_route,
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    idem = "".join(random.choices(string.ascii_uppercase + string.digits, k=6))
    logger.info(f"request_id={idem} start request path={request.url.path}")
    start_time = time.time()

    response = await call_next(request)

    process_time = (time.time() - start_time) * 1000
    formatted_process_time = "{0:.2f}".format(process_time)
    logger.info(
        f"request_id={idem} completed_in={formatted_process_time}ms status_code={response.status_code}"
    )

    return response


app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(todo.router, prefix="/todo", tags=["Todo"])


@app.get("/", include_in_schema=False)
def read_root():
    return {"Hello": "World"}


class StandaloneApplication(BaseApplication):
    def __init__(self, application: Callable, options: Dict[str, Any] = None):
        self.options = options or {}
        self.application = application
        super().__init__()

    def load_config(self):
        config = {
            key: value
            for key, value in self.options.items()
            if key in self.cfg.settings and value is not None
        }
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application


if __name__ == "__main__":
    if not os.environ.get("ENV") == "dev":
        options = {
            "bind": "%s:%s" % ("0.0.0.0", "8001"),
            "workers": 4,
            "worker_class": "uvicorn.workers.UvicornWorker",
            "timeout": 240,
            "graceful_timeout": 240,
            "keepalive": 30,
        }
        StandaloneApplication(app, options).run()
    else:
        uvicorn.run("server:app", port=7777, reload=True)
