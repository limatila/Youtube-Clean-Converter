#uncompressed downloads

from fastapi import APIRouter, BackgroundTasks, HTTPException, Request
from fastapi.responses import FileResponse

from src.services.youtubeDownloaders import download_mp3, download_mp4
from src.services.validators import inputValidation
from src.services.validators.cookieValidation import validate_cookies
from src.services.fileUsage_management import account_for_usage
from src.middleware.loggers import requestsLogger
from src.middleware.requestLimiters import ipLimiter
from src.config import DEFAULT_REQUEST_IP_LIMIT

downloads_router = APIRouter(prefix="/download", tags=['Download'])

@downloads_router.get("/mp3/", description="Downloads a URL's audio in mp3, in browser. Just put a video url in the input to download it (ETA: 20s)")
@ipLimiter.limit(DEFAULT_REQUEST_IP_LIMIT)
def get_in_mp3_audio(request: Request, url: str, background: BackgroundTasks):
    requestsLogger.info(f"New GET request of /download/mp3 for: {url}")
    #for youtube urls: #? other may be added for other sources
    inputValidation.verify_youtube_url(url) 

    #Download
    downloadOutputPath = download_mp3(url)

    # success
    if downloadOutputPath:
        filename = downloadOutputPath.name
        #file usage management
        background.add_task(account_for_usage, downloadOutputPath)
        background.add_task(validate_cookies)

        return FileResponse(
            filename=filename,
            path=downloadOutputPath,
            media_type="audio/mpeg",
            headers={
                "result": "Video has been successfully delivered with .mp3.",
                "hint": "Just open the video with a compatible video player."
            }
        )
    else:
        raise HTTPException(status_code=500, detail="Could not resolve video conversion.")

@downloads_router.get("/mp4/", description="Downloads a URL's video, in browser. Just put a video url in the input to download it (ETA: 8s)")
@ipLimiter.limit(DEFAULT_REQUEST_IP_LIMIT)
def get_in_mp4_video(request: Request, url: str, background: BackgroundTasks):
    requestsLogger.info(f"New GET request of /download/mp4 for: {url}")
    #for youtube urls: #? other may be added for other sources
    inputValidation.verify_youtube_url(url) 

    #Download
    downloadOutputPath = download_mp4(url)

    # success
    if downloadOutputPath:
        filename = downloadOutputPath.name
        #file usage management
        background.add_task(account_for_usage, downloadOutputPath)
        background.add_task(validate_cookies)

        return FileResponse(
            filename=filename,
            path=downloadOutputPath,
            media_type="video/mp4",
            headers={
                "result": "Video has been successfully delivered with .mp4.",
                "hint": "Just open the video with a compatible video player."
            }
        )
    else:
        raise HTTPException(status_code=500, detail="Could not resolve video conversion.")
