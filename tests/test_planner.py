from pathlib import Path 
from munazum.planner import build_plan
from munazum.scanner import FileMetadata


def test_plan_returns_sequence():
    files = []
    output_root = Path("/tmp")

    plan = build_plan(files, output_root)

    assert isinstance(plan, list)


def test_plan_is_list_even_if_empty(tmp_path): 
    plan = build_plan([], tmp_path)
    assert isinstance(plan, list)


def test_plan_items_have_source_and_destination():
    files = [
        FileMetadata(
            path=Path("example.txt"),
            name="example.txt",
            extension=".txt",
            size_bytes=100,
            created_at=0.0,
            modified_at=0.0,
        ),
        FileMetadata(
            path=Path("code.py"),
            name="code.py",
            extension=".py",
            size_bytes=200,
            created_at=0.0,
            modified_at=0.0,
        ),
    ]

    output_root = Path("/tmp")

    plan = build_plan(files, output_root)

    for item in plan:
        assert hasattr(item, "source")
        assert hasattr(item, "destination")
