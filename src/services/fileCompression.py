# File compression scripts, to provide less data usage
from pathlib import Path

from py7zr import SevenZipFile as SZip

from src.config import COMPRESSION_FOLDER_PATH, DEFAULT_COMPRESSION_EXTENSION
from src.middleware.loggers import fileUsageLogger

COMPRESSION_FOLDER_PATH.mkdir(exist_ok=True)

def compress_single_file(file_path: Path, compressionExtension: str = DEFAULT_COMPRESSION_EXTENSION) -> Path:
    try:
        assert file_path.exists()
    except AssertionError:
        fileUsageLogger.error(f"File Compression Service > file to compress could not be found at: {str(file_path.relative_to("./"))}")
        raise AssertionError

    #get folder of path
    outputZipPath: Path = COMPRESSION_FOLDER_PATH / (file_path.stem + compressionExtension)
    
    #Checking if already exists
    if outputZipPath.exists():
        return outputZipPath

    try:
        #for different formats: filename-fileextension.7z
        with SZip(outputZipPath, 'w') as zipfile:
            zipfile.write(file_path, arcname=file_path.name)
        
        assert outputZipPath.exists()
        fileUsageLogger.debug(f"File Compression Service > new file was compressed: {str(outputZipPath.relative_to("./"))}")
    except Exception as err:
        fileUsageLogger.error(f"File Compression Service > error during file compression process: {err.__class__.__name__}. Check uvicorn logs!")
        raise err

    return outputZipPath

#? def compressPlaylistFiles