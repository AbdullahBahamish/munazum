import argparse
import logging
from pathlib import Path
from munazum.scanner import scan_folder
from munazum.planner import build_plan
from munazum.executor import execute_plan
from munazum.ml_stats import StatsAssistant

def configure_logging(verbose: bool) -> None:
    level = logging.INFO if verbose else logging.WARNING
    logging.basicConfig(
        level=level,
        format="%(levelname)s: %(message)s",
    )

def configure_logging(verbose: bool) -> None:
    level = logging.INFO if verbose else logging.WARNING
    logging.basicConfig(
        level=level,
        format="%(levelname)s: %(message)s",
    )


def run_command(args: argparse.Namespace) -> None:
    target_folder = Path(args.target).resolve()
    output_folder = Path(args.output).resolve()

    logging.info(f"Target folder: {target_folder}")
    logging.info(f"Output folder: {output_folder}")

    files = scan_folder(target_folder)
    plan = build_plan(files, output_folder)

    logging.info(f"Planned operations: {len(plan)}")

    if args.dry_run:
        print("DRY RUN — no files will be copied\n")
    execute_plan(plan, dry_run=args.dry_run)

    print("Done.")

    # --- ML suggestions (assistive, read-only) ---
    assistant = StatsAssistant()
    decision_log_path = target_folder / ".munazum_decisions.jsonl"
    assistant.load_log(decision_log_path)

    if plan:
        print("\nML suggestions (assistive only):")
        for item in plan:
            suggestion, confidence = assistant.suggest_category(item.source.name)
            if suggestion and confidence >= 0.6:
                print(
                    f"  - {item.source.name} → {suggestion} "
                    f"(confidence: {confidence:.2f})"
                )



def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="munazum",
        description="Munazum — safe, deterministic folder organiser",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    run_parser = subparsers.add_parser(
        "run",
        help="Organise a folder safely",
    )

    run_parser.add_argument(
        "target",
        help="Target folder to organise",
    )

    run_parser.add_argument(
        "--output",
        default="Organized",
        help="Output folder for organised copy (default: Organized)",
    )

    run_parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview actions without copying files",
    )

    run_parser.add_argument(
        "--verbose",
        action="store_true",
        help="Show detailed logs",
    )

    run_parser.set_defaults(func=run_command)

    return parser


def main() -> None:  # same as void in some languages.
    parser = build_parser()
    args = parser.parse_args()
    configure_logging(args.verbose)
    args.func(args)


if __name__ == "__main__":
    main()