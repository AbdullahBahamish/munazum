from dataclasses import dataclass
from pathlib import Path
from typing import List
from munazum.rules import classify_by_extension, Category
from munazum.scanner import FileMetadata


@dataclass(frozen=True)
class PlanItem:
    """
    Represents a single planned copy operation.
    """
    source: Path
    destination: Path
    category: Category


def build_plan(
    files: List[FileMetadata],
    output_root: Path,
) -> List[PlanItem]:
    """
    Build a dry-run organisation plan.

    - Does NOT touch the filesystem.
    - Uses deterministic rules only.
    - Produces explicit source → destination mappings.
    """
    plan: List[PlanItem] = []

    for file_meta in files:
        category = classify_by_extension(file_meta.path)

        if category == Category.UNKNOWN:
            # Skip unknown files in v0 (explicit choice)
            continue

        category_folder = output_root / category.value
        destination_path = category_folder / file_meta.name

        plan.append(
            PlanItem(
                source=file_meta.path,
                destination=destination_path,
                category=category,
            )
        )

    return plan
