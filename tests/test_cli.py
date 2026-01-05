import argparse
from pathlib import Path
from unittest.mock import patch, MagicMock

from munazum.cli import build_parser, run_command


def test_parser_parses_run_command():
    parser = build_parser()

    args = parser.parse_args([
        "run",
        "test_folder",
        "--dry-run",
        "--verbose",
    ])

    assert args.command == "run"
    assert args.target == "test_folder"
    assert args.dry_run is True
    assert args.verbose is True


@patch("munazum.cli.execute_plan")
@patch("munazum.cli.build_plan")
@patch("munazum.cli.scan_folder")
def test_run_command_dry_run(
    mock_scan_folder,
    mock_build_plan,
    mock_execute_plan,
):
    # Arrange
    args = argparse.Namespace(
        target="input",
        output="output",
        dry_run=True,
        verbose=False,
    )

    fake_files = [MagicMock()]
    fake_plan = []

    mock_scan_folder.return_value = fake_files
    mock_build_plan.return_value = fake_plan

    # Act
    run_command(args)

    # Assert
    mock_scan_folder.assert_called_once_with(Path("input").resolve())
    mock_build_plan.assert_called_once()
    mock_execute_plan.assert_called_once_with(fake_plan, dry_run=True)
