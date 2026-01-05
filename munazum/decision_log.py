import json
from dataclasses import asdict
from pathlib import Path
from typing import Dict, Any
from datetime import datetime
from munazum.planner import PlanItem


LOG_FILENAME = ".munazum_decisions.jsonl"

def log_decision(
    plan_item: PlanItem,
    accepted: bool,
    extra_features: Dict[str, Any] | None = None,
    log_dir: Path | None = None,
) -> None:

    """
    Append a single decision record to the local decision log.

    This file is:
    - local only
    - append-only
    - human-readable
    """
    
    record = {
        "timestamp": datetime.utcnow().isoformat(),
        "source": str(plan_item.source),
        "destination": str(plan_item.destination),
        "category": plan_item.category.value,
        "accepted": accepted,
    }

    if extra_features:
        record["features"] = extra_features

    base_dir = log_dir if log_dir else plan_item.source.parent
    log_path = base_dir / LOG_FILENAME

    with log_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record) + "\n")
