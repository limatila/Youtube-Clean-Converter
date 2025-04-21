from yt_dlp import YoutubeDL
from pathlib import Path

from src.services.validators.cookieValidation import validate_cookies

from src.config import YDL_OPTS
from src.config import DOWNLOADS_FOLDER_PATH_MP3
from src.middleware.loggers import fileUsageLogger

DOWNLOADS_FOLDER_PATH_MP3.mkdir(exist_ok=True)

#*- to mp3
def download_mp3(url: str, _retry_flag: bool = False) -> Path:
    try:
        with YoutubeDL(YDL_OPTS['SINGLE_MP3']) as ydl:
            video = ydl.extract_info(url, download=True)
            file_path = Path(ydl.prepare_filename(video)).with_suffix('.mp3')
        fileUsageLogger.debug(f"File Download Service (mp3) > new file was downloaded: {str(file_path.relative_to("./"))}")
    except Exception as err:
        if not _retry_flag:
            validate_cookies()  # check if cookies was corrupted
            return download_mp3(url=url, _retry_flag=True)
        else:
            fileUsageLogger.error(f"File Download Service (mp3) > error during file download process: {err.__class__.__name__}. Check uvicorn logs!")
            raise err
        
    # sucess 
    #BUG: some characters in video titles are bugged out when downloading, like ':', so it will return a RuntimeError
    validate_cookies() #? later add this as a decorator
    return file_path #returns full path in str
    
#*- to mp4
def download_mp4(url: str, _retry_flag: bool = False) -> Path:
    try:
        with YoutubeDL(YDL_OPTS['SINGLE_MP4']) as ydl:
            #! need to change aproach
            video = ydl.extract_info(url, download=True)
            file_path = Path(ydl.prepare_filename(video)).with_suffix('.mp4')
        fileUsageLogger.debug(f"File Download Service (mp4) > new file was downloaded: {str(file_path.relative_to("./"))}")
    except Exception as err:
        if not _retry_flag:
            validate_cookies()  # check if cookies was corrupted
            return download_mp4(url=url, _retry_flag=True)
        else:
            fileUsageLogger.error(f"File Download Service (mp4) > error during file download process: {err.__class__.__name__}. Check uvicorn logs!")
            raise err
    
    # sucess 
    #BUG: same as in line 28
    validate_cookies()
    return file_path #returns full path in str
    