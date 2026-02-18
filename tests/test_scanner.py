from pathlib import Path
import os
import pytest

from munazum.scanner import scan_folder, FileMetadata


def create_file(path: Path, name: str, content: str = "x") -> Path:
    p = path / name
    p.write_text(content)
    return p


def test_scan_raises_if_folder_missing(tmp_path: Path):
    with pytest.raises(FileNotFoundError):
        scan_folder(tmp_path / "missing")


def test_scan_raises_if_not_directory(tmp_path: Path):
    file = create_file(tmp_path, "file.txt")
    with pytest.raises(NotADirectoryError):
        scan_folder(file)


def test_default_scan_is_non_recursive(tmp_path: Path):
    create_file(tmp_path, "a.txt")
    sub = tmp_path / "sub"
    sub.mkdir()
    create_file(sub, "b.txt")

    results = scan_folder(tmp_path)
    names = {f.name for f in results}

    assert names == {"a.txt"}


def test_recursive_scan_includes_subfolder(tmp_path: Path):
    create_file(tmp_path, "a.txt")
    sub = tmp_path / "sub"
    sub.mkdir()
    create_file(sub, "b.txt")

    results = scan_folder(tmp_path, recursive=True)
    names = {f.name for f in results}

    assert names == {"a.txt", "b.txt"}


def test_max_depth_limits_recursion(tmp_path: Path):
    create_file(tmp_path, "root.txt")

    lvl1 = tmp_path / "lvl1"
    lvl1.mkdir()
    create_file(lvl1, "l1.txt")

    lvl2 = lvl1 / "lvl2"
    lvl2.mkdir()
    create_file(lvl2, "l2.txt")

    results = scan_folder(tmp_path, recursive=True, max_depth=1)
    names = {f.name for f in results}

    assert "root.txt" in names
    assert "l1.txt" in names
    assert "l2.txt" not in names


def test_ignored_folders_are_skipped(tmp_path: Path):
    create_file(tmp_path, "a.txt")
    ignored = tmp_path / "skipme"
    ignored.mkdir()
    create_file(ignored, "b.txt")

    results = scan_folder(
        tmp_path,
        recursive=True,
        ignored_folders={"skipme"},
    )

    names = {f.name for f in results}
    assert names == {"a.txt"}


def test_metadata_fields_are_correct(tmp_path: Path):
    f = create_file(tmp_path, "Doc.PDF", "data")

    result = scan_folder(tmp_path)[0]

    assert isinstance(result, FileMetadata)
    assert result.name == "Doc.PDF"
    assert result.extension == ".pdf"
    assert result.size_bytes == len("data")
    assert result.path == f.resolve()
    assert result.created_at > 0
    assert result.modified_at > 0


@pytest.mark.skipif(os.name == "nt", reason="Symlinks require admin privileges on Windows")
def test_symlinks_are_ignored(tmp_path: Path):
    real = create_file(tmp_path, "real.txt")
    link = tmp_path / "link.txt"
    link.symlink_to(real)

    results = scan_folder(tmp_path, recursive=True)
    names = {f.name for f in results}

    assert "real.txt" in names
    assert "link.txt" not in names
