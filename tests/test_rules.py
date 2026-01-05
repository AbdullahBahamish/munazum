from pathlib import Path 

from munazum.rules import (
    classify_by_extension,
    Category,
)

def test_documents():
    assert classify_by_extension(Path("file.pdf")) == Category.DOCUMENTS
    assert classify_by_extension(Path("report.docx")) == Category.DOCUMENTS 
    assert classify_by_extension(Path("notes.txt")) == Category.DOCUMENTS

    
def test_code_files():
    assert classify_by_extension(Path("script.py")) == Category.CODE
    assert classify_by_extension(Path("main.cpp")) == Category.CODE
    assert classify_by_extension(Path("app.js")) == Category.CODE


def test_videos():
    assert classify_by_extension(Path("movie.mp4")) == Category.VIDEOS
    assert classify_by_extension(Path("clip.mkv")) == Category.VIDEOS


def test_audios():
    assert classify_by_extension(Path("voice.mp3")) == Category.AUDIOS
    assert classify_by_extension(Path("sound.wav")) == Category.AUDIOS


def test_executables():
    assert classify_by_extension(Path("installer.exe")) == Category.EXECUTABLES
    assert classify_by_extension(Path("run.bat")) == Category.EXECUTABLES


def test_archives():
    assert classify_by_extension(Path("data.zip")) == Category.ARCHIVES
    assert classify_by_extension(Path("backup.7z")) == Category.ARCHIVES


def test_unknown_files():
    assert classify_by_extension(Path("file.xyz")) == Category.UNKNOWN
    assert classify_by_extension(Path("README")) == Category.UNKNOWN


def test_case_insensitivity():
    assert classify_by_extension(Path("VIDEO.MP4")) == Category.VIDEOS
    assert classify_by_extension(Path("SCRIPT.PY")) == Category.CODE