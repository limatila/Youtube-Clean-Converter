from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware

from src.routers import *
from src.config import API_DETAILS
from src.services.validators.cookieValidation import validate_cookies
from src.middleware.requestLimiters import globalLimiter
from src.middleware.loggers import _initLoggers

#settup loggers and create files
_initLoggers()

#API definition
app = FastAPI (
    version=API_DETAILS['version'],
    title=API_DETAILS['name'],
    summary=API_DETAILS['summary'],
    description=API_DETAILS['description_md']
)
app.state.limiter = globalLimiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)

app.include_router(downloads_router)
app.include_router(compressions_router)
app.include_router(swagger_router)

# startup
if __name__ == "__main__":
    validate_cookies()