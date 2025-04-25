from slowapi import Limiter
from slowapi.util import get_remote_address

from src.config import (
    DEFAULT_REQUEST_IP_LIMIT, 
    DEFAULT_REQUEST_GLOBAL_LIMIT,
)

def get_global_key():
    return True

# Applying limit to request by ip
ipLimiter = Limiter(key_func=get_remote_address, default_limits=[DEFAULT_REQUEST_IP_LIMIT])

# Applying to more than one ip (multiple Ip DDoS protection)
globalLimiter = Limiter(key_func=get_global_key, default_limits=[DEFAULT_REQUEST_GLOBAL_LIMIT])