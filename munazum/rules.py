from enum import Enum 
from pathlib import Path
from typing import Dict, Set

class Category(str, Enum):
    DOCUMENTS = "documents"
    CODE = "code"
    VIDEOS = "videos"
    AUDIOS = "audios"
    EXECUTABLES = "executables"
    ARCHIVES = "archives"
    UNKNOWN = "unknown"

# ---- Extention mapping (deterministic, explicit) ----

DOCUMENT_EXTENSIONS: Set[str] = {
    ".pdf", ".doc", ".docx", ".txt", ".md", ".rtf"
}

CODE_EXTENSIONS: Set[str] = {
    ".py", ".cpp", ".c", ".h", ".hpp", ".java", ".js",
    ".ts", ".go", ".rs", ".cs", ".php", ".sh"
}

VIDEO_EXTENSIONS: Set[str] = {
    ".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv"
}

AUDIO_EXTENSIONS: Set[str] = {
    ".mp3", ".wav", ".aac", ".flac", ".ogg"
}

EXECUTABLE_EXTENSIONS: Set[str] = {
    ".exe", ".msi", ".bat", ".cmd"
}

ARCHIVE_EXTENSIONS: Set[str] = {
    ".zip", ".rar", ".7z", ".tar", ".gz"
}


# ---- Core rule engine ----

EXTENSTION_CATEGORY_MAP: Dict[Category, Set[str]] = {
    Category.DOCUMENTS: DOCUMENT_EXTENSIONS,
    Category.CODE: CODE_EXTENSIONS,
    Category.VIDEOS: VIDEO_EXTENSIONS,
    Category.AUDIOS: AUDIO_EXTENSIONS,
    Category.EXECUTABLES: EXECUTABLE_EXTENSIONS,
    Category.ARCHIVES: ARCHIVE_EXTENSIONS,
}


def classify_by_extension(file_path: Path) -> Category:
    """
    Classify a file into a category based purely on its extension. 

    This function is deterministic and side-effect free.
    """
    suffix = file_path.suffix.lower()

    for category, extensions in EXTENSTION_CATEGORY_MAP.items():
        if suffix in extensions:
            return category
        
    return Category.UNKNOWN

def is_suppported(file_path: Path) -> bool:
    """
    Return True if the file belongs to a known category.
    """
    return classify_by_extension(file_path) != Category.UNKNOWN

