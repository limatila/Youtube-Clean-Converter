
# loggers to be used in one of these situations: cookie validation, performance issues, (...)

import logging
from logging import StreamHandler, FileHandler, Formatter

from src.config import (
    BASE_LOGS_PATH,
    defaultFormatter, 
    friendlyStreamFormatter,
)
performancePath: str = BASE_LOGS_PATH + 'performance.log'
cookiesPath: str = BASE_LOGS_PATH + 'cookies.log'
fileUsagePath: str = BASE_LOGS_PATH + 'fileUsage.log'
requestsPath: str = BASE_LOGS_PATH + 'requests.log'

performanceLogger = logging.getLogger('performance_log')    # performance tracking, SlowApi
cookiesLogger = logging.getLogger('cookies_log')      # cookieValidation
fileUsageLogger = logging.getLogger('fileUsage_log') # file usage management, download / compression
requestsLogger = logging.getLogger('requests_log')  # requests related information

#TODO: reimplement logger initialization, it is incoherent and repetitive!
def _initLoggers():
    #Base config
    logging.basicConfig(encoding='UTF-8', level=logging.DEBUG, format=defaultFormatter)

    for logger in [performanceLogger, cookiesLogger, fileUsageLogger, requestsLogger]:
        logger.handlers.clear()
        logger.propagate = False

    #configuring Performance logger: file + stream
    performance_FileHandler = FileHandler(performancePath)
    performance_FileHandler.setLevel(logging.INFO)
    performance_FileHandler.setFormatter(Formatter(defaultFormatter))
    performance_StreamHandler = StreamHandler()
    performance_StreamHandler.setLevel(logging.WARNING)
    performance_StreamHandler.setFormatter(Formatter(friendlyStreamFormatter))

    performanceLogger.addHandler(performance_FileHandler)
    performanceLogger.addHandler(performance_StreamHandler)
    
    #configuring Cookies logger: file only
    cookies_FileHandler = FileHandler(cookiesPath)
    cookies_FileHandler.setLevel(logging.DEBUG)
    cookies_FileHandler.setFormatter(Formatter(defaultFormatter))

    cookiesLogger.addHandler(cookies_FileHandler)

    #configuring File Usage logger: file + stream
    fileUsage_FileHandler = FileHandler(fileUsagePath)
    fileUsage_FileHandler.setLevel(logging.DEBUG)
    fileUsage_FileHandler.setFormatter(Formatter(defaultFormatter))
    fileUsage_StreamHandler = StreamHandler()
    fileUsage_StreamHandler.setLevel(logging.WARNING)
    fileUsage_StreamHandler.setFormatter(Formatter(friendlyStreamFormatter))

    fileUsageLogger.addHandler(fileUsage_FileHandler)
    fileUsageLogger.addHandler(fileUsage_StreamHandler)

    #Configuring Requests logger: file + stream
    requestsFileHandler = FileHandler(requestsPath)
    requestsFileHandler.setLevel(logging.INFO)
    requestsFileHandler.setFormatter(Formatter(defaultFormatter))
    requestsStreamHandler = StreamHandler()
    requestsStreamHandler.setLevel(logging.DEBUG)
    requestsStreamHandler.setFormatter(Formatter(friendlyStreamFormatter))

    requestsLogger.addHandler(requestsFileHandler)
    requestsLogger.addHandler(requestsStreamHandler)


#! need test in aws, remove try except if not necessary.
# try:
# _initLoggers();
# except FileNotFoundError:
#     from pathlib import Path
#     #create non-existant dirs and files
#     loggersList: list[logging.Logger] = [performanceLogger, cookiesLogger, fileUsagePath, requestsPath]

#     for logger in loggersList:
#         Path(logger).parent.mkdir(exist_ok=True, parents=True)

#         currentFile = list(filter(lambda x: isinstance(x, FileHandler), logger.handlers))[0].baseFilename
#         if not Path(currentFile).exists():
#             Path(currentFile).write_text("")
#     #try again
#     _initLoggers();


if __name__ == "__main__":
    _initLoggers()

    performanceLogger.warning("TESTING performance monitoring logs")
    cookiesLogger.info("TESTING cookie management logs")
    fileUsageLogger.info("TESTING file usage management logs")
    requestsLogger.info("TESTING request logs")

    #* cookie limited level: DEBUG
    cookiesLogger.debug("TESTING cookie debug")
    #* performance limited level: file/INFO, stream/WARNING
    performanceLogger.debug("TESTING performance debug") #will not be logged
    performanceLogger.info("TESTING performance info")
    #* file usage limited level: file/DEBUG, stream/WARNING
    fileUsageLogger.debug("TESTING file usage debug") #only to file
    fileUsageLogger.warning("TESTING file usage warning")   #to file and stream
    #* requests limited level: file/INFO, stream/DEBUG
    requestsLogger.debug("TESTING requests debug") #only to stream
    requestsLogger.info("TESTING requests info")   #to file and stream

    for logger in [performanceLogger, cookiesLogger, fileUsageLogger, requestsLogger]:
        print(logger.handlers)