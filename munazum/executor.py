from pathlib import Path
from typing import List
import shutil
import logging

from munazum.planner import PlanItem
from munazum.decision_log import log_decision

logger = logging.getLogger(__name__)

def execute_plan(plan: List[PlanItem], dry_run: bool = False) -> None:
    """
    Execute a copy plan safely.

    - Copies files only (no move, no delete).
    - Creates destination directories if needed.
    - Refuses to overwrite existing files.
    - Logs accepted decisions (non-dry-run only).
    """
    for item in plan:
        source = item.source
        destination = item.destination

        if not source.exists():
            logger.warning(f"Source missing, skipping: {source}")
            continue

        if destination.exists():
            logger.warning(f"Destination exists, skipping: {destination}")
            continue

        logger.info(f"{'DRY-RUN: ' if dry_run else ''}Copying {source} -> {destination}")

        if dry_run:
            continue

        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)

        # ML signal: this decision was accepted
        log_decision(
            plan_item=item,
            accepted=True,
        )
