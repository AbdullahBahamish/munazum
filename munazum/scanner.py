from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional
import os


@dataclass(frozen=True)
class FileMetadata:
    """
    Immutable representation of a file on disk.
    """
    path: Path
    name: str
    extension: str
    size_bytes: int
    created_at: float
    modified_at: float


def scan_folder(
    target_folder: Path,
    *,
    recursive: bool = False,
    max_depth: Optional[int] = None,
    ignored_folders: Optional[set[str]] = None,
) -> List[FileMetadata]:
    """
    Scan a folder and collect metadata for files.

    Default behaviour (SAFE):
    - Scans ONLY files directly inside target_folder
    - Does NOT enter subfolders

    Optional:
    - recursive=True enables controlled recursion
    - max_depth limits traversal depth

    Guarantees:
    - Ignores directories
    - Does NOT follow symlinks
    - Has no side effects
    """
    if not target_folder.exists():
        raise FileNotFoundError(f"Folder does not exist: {target_folder}")

    if not target_folder.is_dir():
        raise NotADirectoryError(f"Not a directory: {target_folder}")

    if max_depth is None:
        max_depth = 100 if recursive else 0

    ignored_folders = ignored_folders or set()
    results: List[FileMetadata] = []

    def _scan(path: Path, depth: int) -> None:
        for entry in path.iterdir():
            if entry.is_dir():
                if not recursive or depth >= max_depth:
                    continue
                if entry.name in ignored_folders:
                    continue
                _scan(entry, depth + 1)

            elif entry.is_file() and not entry.is_symlink():
                try:
                    stat = entry.stat()
                except OSError:
                    continue

                results.append(
                    FileMetadata(
                        path=entry.resolve(),
                        name=entry.name,
                        extension=entry.suffix.lower(),
                        size_bytes=stat.st_size,
                        created_at=getattr(stat, "st_birthtime", stat.st_ctime),
                        modified_at=stat.st_mtime,
                    )
                )

    _scan(target_folder, depth=0)
    return results