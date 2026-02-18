from pathlib import Path
import pytest
from munazum.executor import execute_plan
from munazum.planner import PlanItem
from munazum.rules import Category

def test_execute_plan_moves_file(tmp_path):
    # Setup
    source_dir = tmp_path / "source"
    source_dir.mkdir()
    target_dir = tmp_path / "Organized"
    
    file_path = source_dir / "test.txt"
    file_path.write_text("hello")
    
    dest_path = target_dir / "documents" / "txt" / "test.txt"
    
    plan = [
        PlanItem(
            source=file_path,
            destination=dest_path,
            category=Category.DOCUMENTS
        )
    ]
    
    # Execute
    execute_plan(plan, dry_run=False)
    
    # Verify
    assert not file_path.exists()  # Should be moved
    assert dest_path.exists()
    assert dest_path.read_text() == "hello"

def test_execute_plan_dry_run_does_nothing(tmp_path):
    # Setup
    source_dir = tmp_path / "source"
    source_dir.mkdir()
    target_dir = tmp_path / "Organized"
    
    file_path = source_dir / "test.txt"
    file_path.write_text("hello")
    
    dest_path = target_dir / "documents" / "txt" / "test.txt"
    
    plan = [
        PlanItem(
            source=file_path,
            destination=dest_path,
            category=Category.DOCUMENTS
        )
    ]
    
    # Execute
    execute_plan(plan, dry_run=True)
    
    # Verify
    assert file_path.exists()  # Should NOT be moved
    assert not dest_path.exists()

def test_execute_plan_skips_existing_destination(tmp_path):
    # Setup
    source_dir = tmp_path / "source"
    source_dir.mkdir()
    target_dir = tmp_path / "Organized"
    
    file_path = source_dir / "test.txt"
    file_path.write_text("new content")
    
    dest_path = target_dir / "documents" / "txt" / "test.txt"
    dest_path.parent.mkdir(parents=True)
    dest_path.write_text("old content")
    
    plan = [
        PlanItem(
            source=file_path,
            destination=dest_path,
            category=Category.DOCUMENTS
        )
    ]
    
    # Execute
    execute_plan(plan, dry_run=False)
    
    # Verify
    assert file_path.exists()  # Should NOT be moved (skip existing)
    assert dest_path.read_text() == "old content"