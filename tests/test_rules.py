from pathlib import Path
from munazum.rules import classify_by_extension, Category


def test_known_document_extension():
    assert classify_by_extension(Path("file.pdf")) == Category.DOCUMENTS


def test_known_code_extension():
    assert classify_by_extension(Path("main.py")) == Category.CODE


def test_unknown_extension():
    assert classify_by_extension(Path("file.xyz")) == Category.OTHERS


def test_image_extension():
    assert classify_by_extension(Path("photo.jpg")) == Category.IMAGES


def test_extension_matching_is_case_insensitive():
    assert classify_by_extension(Path("README.MD")) == Category.DOCUMENTS
