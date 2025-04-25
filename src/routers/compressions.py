# downloads with compression

from fastapi import APIRouter, BackgroundTasks, HTTPException, Request
from fastapi.responses import FileResponse

from src.services.youtubeDownloaders import download_mp3, download_mp4
from src.services.fileCompression import compress_single_file
from src.services.validators import inputValidation
from src.services.validators.cookieValidation import validate_cookies
from src.services.fileUsage_management import account_for_usage
from src.middleware.requestLimiters import ipLimiter
from src.middleware.loggers import requestsLogger
from src.config import DEFAULT_REQUEST_IP_LIMIT

compressions_router = APIRouter(prefix="/compressed", tags=['Compressed'])

@compressions_router.get("/mp3/", description="Downloads a URL's audio in a compressed file, in browser. Just put a video url in the input to download it (ETA: 20s)")
@ipLimiter.limit(DEFAULT_REQUEST_IP_LIMIT)
def get_compressed_in_mp3(request: Request, url: str, background: BackgroundTasks):
    requestsLogger.info(f"New GET request of /compressed/mp3 for: {url}")
    #for youtube urls: #? other may be added for other sources
    inputValidation.verify_youtube_url(url) 

    #Download
    downloadOutputPath = download_mp3(url)

    #Compression
    compressedOutputPath = compress_single_file(downloadOutputPath)

    # success
    if downloadOutputPath:
        filename = compressedOutputPath.name
        #file usage management
        background.add_task(account_for_usage, downloadOutputPath)
        background.add_task(validate_cookies)

        return FileResponse(
            filename=filename,
            path=compressedOutputPath,
            media_type="application/x-7z-compressed",
            headers={
                "result": "Video has been successfully delivered with .mp3, and compressed for delivery.",
                "hint": "Please extract the .mp3 audio to access your audio"
            }
        )
    else:
        raise HTTPException(status_code=500, detail="Could not resolve video conversion.")

@compressions_router.get("/mp4/", description="Downloads a URL's video in a compressed file, in browser. Just put a video url in the input to download it (ETA: 20s)")
@ipLimiter.limit(DEFAULT_REQUEST_IP_LIMIT)
def get_compressed_in_mp4(request: Request, url: str, background: BackgroundTasks):
    requestsLogger.info(f"New GET request of /compressed/mp4 for: {url}")
    #for youtube urls: #? other may be added for other sources
    inputValidation.verify_youtube_url(url) 

    #Download
    downloadOutputPath = download_mp4(url)

    #Compression
    compressedOutputPath = compress_single_file(downloadOutputPath)

    # success
    if downloadOutputPath:
        filename = compressedOutputPath.name
        #file usage management
        background.add_task(account_for_usage, downloadOutputPath)
        background.add_task(validate_cookies)

        return FileResponse(
            filename=filename,
            path=compressedOutputPath,
            media_type="application/x-7z-compressed",
            headers={
                "result": "Video has been successfully delivered with .mp3, and compressed for delivery.",
                "hint": "Please extract the .mp4 video to access your video"
            }
        )
    else:
        raise HTTPException(status_code=500, detail="Could not resolve video conversion.")
