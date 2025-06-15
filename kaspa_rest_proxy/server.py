import importlib
import logging
import os
import pkgutil

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse

from kaspa_rest_proxy import endpoints
from kaspa_rest_proxy.kaspad.kaspad_rpc_client import kaspad_rpc_client
from kaspa_rest_proxy.logging import setup_logging
from kaspa_rest_proxy.middleware.StrictRoute import StrictRoute

setup_logging()

_logger = logging.getLogger(__name__)

app = FastAPI(
    title="kaspa-rest-proxy",
    description="REST to Kaspad wRPC Proxy\n\n"
    "[https://github.com/supertypo/kaspa-rest-proxy](https://github.com/supertypo/kaspa-rest-proxy)",
    version=os.getenv("VERSION") or "dev",
    contact={"name": "suprtypo@pm.me"},
    license_info={"name": "MIT"},
    docs_url="/",
    redoc_url=None,
    swagger_ui_parameters={"tryItOutEnabled": True},
)
app.router.route_class = StrictRoute  # type: ignore[attr-defined]

app.add_middleware(GZipMiddleware, minimum_size=500)  # type: ignore[arg-type]

app.add_middleware(
    CORSMiddleware,  # type: ignore[arg-type]
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Automatically include all routers from the `endpoints` package
for _, module_name, _ in pkgutil.iter_modules(endpoints.__path__):
    module_path = f"{endpoints.__name__}.{module_name}"
    try:
        module = importlib.import_module(module_path)
        if hasattr(module, "router"):
            app.include_router(module.router)
            _logger.info(f"Registered router from module: {module_path}")
        else:
            _logger.debug(f"Module {module_path} has no 'router', skipping")
    except Exception as e:
        _logger.exception(f"Failed to import router from {module_path}: {e}")


@app.on_event("startup")
async def warm_up():
    await kaspad_rpc_client()


@app.exception_handler(Exception)
async def unicorn_exception_handler(_request: Request, exception: Exception):
    return JSONResponse(status_code=400, content={"detail": str(exception)})
