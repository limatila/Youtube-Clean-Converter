
# functions that check cookie usage, as requests are added

from src.config import (
    COOKIES_FILE_PATH, 
    COOKIES_BACKUP_FILE_PATH
)
from src.middleware.loggers import cookiesLogger
from src.exceptions import CookieNotFound

#should run one per request, to be correctly used
def update_cookies():
    try:
        with open(COOKIES_BACKUP_FILE_PATH, 'r') as backup:
            with open(COOKIES_FILE_PATH, 'w') as cookies:
                backupLines = backup.read()
                cookies.write(backupLines)
                cookiesLogger.debug(f"Changes in {COOKIES_FILE_PATH} detected; Cookiefile was updated with backup.")
    except FileNotFoundError as err:
        errorMessage = f"Cookiefile was not found in path {err.filename}, and is needed. For info in how to extract cookies, go to \'https://github.com/yt-dlp/yt-dlp/wiki/Extractors#exporting-youtube-cookies\'"
        cookiesLogger.error(errorMessage)
        raise CookieNotFound(errorMessage)

def validate_cookies():
    try: 
        with open(COOKIES_FILE_PATH, 'r') as cookies:
            with open(COOKIES_BACKUP_FILE_PATH, 'r') as backup:
                currentLines = cookies.read()
                backupLines = backup.read()
                if currentLines != backupLines: update_cookies()
    except FileNotFoundError as err:
        errorMessage = f"Cookiefile was not found in path {err.filename}, and is needed. For info in how to extract cookies, go to \'https://github.com/yt-dlp/yt-dlp/wiki/Extractors#exporting-youtube-cookies\'"
        cookiesLogger.error(errorMessage)
        raise CookieNotFound(errorMessage)