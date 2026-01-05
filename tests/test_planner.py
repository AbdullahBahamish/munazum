from pathlib import Path 
from munazum.planner import build_plan

def test_plan_returns_sequence():
    files = []
    output_root = Path("/tmp")

    plan = build_plan(files, output_root)

    assert isinstance(plan, list)


def test_plan_is_list_even_if_empty(tmp_path): 
    plan = build_plan([], tmp_path)
    assert isinstance(plan, list)


def test_plan_items_have_source_and_target():
    files = [ 
        Path("example.txt"),
        Path("code.py"),
    ]
    output_root = Path("/tmp") 

    assert isinstance(files, output_root)

    for item in :
        assert hasattr(item, "source")
        assert hasattr(item, "target")