
#* Configurations for the project (mainly: names and paths)
from pathlib import Path

#API names, version, etc..
API_DETAILS: dict[str, str] = {
    "version": "v1.3",
    "name": "Youtube Clean Converter",
    "summary": "An API for automatic download and conversion of Youtube videos, to Audio (.mp3) or Video (.mp4).",
    "description_md": (
        """<br>
### We're in:
 the documentation page of this API, where you can use/test our services
## How to use:
1. Copy a Youtube video link (in Youtube itself) of the video you want to download
2. Select a service in '**Download**' or '**Compressed**', you can use all of the services listed as *GET* methods
    - <i>this API limits requests up to 10 requests per minute.</i> 
3. Press the '**Try it out**' button to be able to input your URL
4. Press '**Execute**', and wait for download
5. You can get your video/audio bellow '*Responses*' section, at a button called '**Download file**'

- *more help?* -> You can check a video that show the usage of this API in the **LINKS** section bellow.

### **Links:**
- [The github source code](https://github.com/limatila/Youtube-Clean-Converter) 
- [A linkedin post that explains how to use the api](https://www.linkedin.com/feed/update/urn:li:ugcPost:7317375614452170752/) 
- [YT-DLP, the tool used to download the videos for this api](https://github.com/yt-dlp/yt-dlp)
- Email me: [atilalimade@gmail.com](mailto:atilalimade@gmail.com)
- [Create an issue (for future fix)](https://github.com/limatila/Youtube-Clean-Converter/issues/new)

<br>
- <b>NOTE:</b>
 you should note that this API doesn't have a HTTPS certificate, but use it in mind that IT SHOULD ONLY download MP3, MP4, and 7z (compressed audio and video) files. Use this as your will.
- <b>NOTE 2:</b>
 as consequence of the first note, please only make HTTP requests, for now (don't let your broswer include https://, but http:// in the start of the url). """
    )
}

#Cookies for youtube client
COOKIES_FILE_PATH = "cookies.txt"
COOKIES_BACKUP_FILE_PATH = "backup-cookies.txt"

#Download and Compression configuration
DOWNLOADS_FOLDER_PATH_MP3 = Path("./mp3-downloads")
DOWNLOADS_FOLDER_PATH_MP4 = Path("./mp4-downloads")
COMPRESSION_FOLDER_PATH = Path("./file-compressions")

QUIET_EXECUTION_OPTION: bool = True #no logs from yt-dlp if True

YDL_OPTS: dict[ str, dict[str, any] ] = {
    #a group of yt-dlp options to be used in downloads methods.
    #shall be used in 'YoutubeDL(YDL_OPTS['your-option'])'.
    'SINGLE_MP3': {
        'format': 'bestaudio[abr=256]/bestaudio[abr<=192]/best',
        'outtmpl': str(DOWNLOADS_FOLDER_PATH_MP3 / '%(title)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'cookiefile': COOKIES_FILE_PATH,
        'noplaylist': True,
        'age_limit': 20,
        'wait_for_video': (0, 86400), #For lives that didn't finish (but will), will wait for 24hours for it to finish.
        'quiet': QUIET_EXECUTION_OPTION
    },
    'SINGLE_MP4': {
        'format': 'bestvideo[ext=mp4][height<=720][fps<=60]+bestaudio/best[ext=mp4][height<=720][fps<=60]/best',
        'outtmpl': str(DOWNLOADS_FOLDER_PATH_MP4 / '%(title)s.%(ext)s'),
        'cookiefile': COOKIES_FILE_PATH,
        'noplaylist': True,
        'age_limit': 20,
        'merge_output_format': 'mp4',
        'wait_for_video': (0, 86400),
        'quiet': QUIET_EXECUTION_OPTION
    }
    # 'MULTIPLE_MP3': 
}

#File usage registry
USAGE_REG_PATH_MP3 = "./src/logs/usage-reg_mp3.json"
USAGE_REG_PATH_MP4 = "./src/logs/usage-reg_mp4.json"
USAGE_REG_INDENT = 2
USAGE_REG_EXECUTIONS_KEY = "executedTimes"
DEFAULT_FILE_EXTENSION = ".mp3"
DEFAULT_COMPRESSION_EXTENSION = '.7z'

#* Logger configuration (paths and formats)
BASE_LOGS_PATH: str = "./src/logs/"
defaultFormatter = '%(asctime)s - %(levelname)s - %(message)s'
friendlyStreamFormatter = '%(levelname)s:     %(message)s - at %(asctime)s in runtime.' #? can be updated to include colors

#DateTime configs
defaultTimezone = "-03:00" #! not used, need fix
defaultTimeFormat = "%d-%m(%y) %H:%M:%S"

#SlowAPI - request limiter
DEFAULT_REQUEST_IP_LIMIT: str = "10/minute" # can be 20/second, 2/minute...
DEFAULT_REQUEST_GLOBAL_LIMIT: str = "100/minute" # you can elevate this for high usage basis