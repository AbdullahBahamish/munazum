from dataclasses import dataclass
from pathlib import Path
from typing import List
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


def scan_folder(target_folder: Path) -> List[FileMetadata]:
    """
    Scan a folder recursively and collect metadata for all files inside it.

    - Operates ONLY within the given folder.
    - Ignores directories.
    - Does NOT follow symlinks.
    - Has no side effects.
    """
    if not target_folder.exists():
        raise FileNotFoundError(f"Folder does not exist: {target_folder}")

    if not target_folder.is_dir():
        raise NotADirectoryError(f"Not a directory: {target_folder}")

    results: List[FileMetadata] = []

    for root, _, file_names in os.walk(target_folder, followlinks=False):
        for file_name in file_names:
            file_path = Path(root) / file_name

            try:
                stat = file_path.stat()
            except OSError:
                # Skip files we cannot access
                continue

            results.append(
                FileMetadata(
                    path=file_path.resolve(),
                    name=file_path.name,
                    extension=file_path.suffix.lower(),
                    size_bytes=stat.st_size,
                    created_at=getattr(stat, "st_birthtime", stat.st_birthtime),
                    modified_at=stat.st_mtime,
                )
            )

    return results