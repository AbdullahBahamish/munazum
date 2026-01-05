import json
from pathlib import Path
from collections import defaultdict
from typing import Dict


LOG_FILENAME = ".munazum_decisions.jsonl"


class StatsAssistant:
    """
    Lightweight, explainable ML assistant based on decision frequencies.
    """

    def __init__(self) -> None:
        self.extension_category_counts: Dict[str, Dict[str, int]] = defaultdict(lambda: defaultdict(int))
        self.total_by_extension: Dict[str, int] = defaultdict(int)

    def load_log(self, log_path: Path) -> None:
        if not log_path.exists():
            return 

        with log_path.open("r", encoding="utf-8") as f:
            for line in f:
                record = json.loads(line)

                source = Path(record["source"])
                category = record["category"]
                accepted = record["accepted"]

                if not accepted:
                    continue

                ext = source.suffix.lower()
                self.extension_category_counts[ext][category] += 1
                self.total_by_extension[ext] += 1

    def suggest_category(self, filename: str) -> tuple[str | None, float]:
        """
        Return (suggested_category, confidence) based on past approvals.
        """
        ext = Path(filename).suffix.lower()

        if ext not in self.total_by_extension:
            return None, 0.0

        category_counts = self.extension_category_counts[ext]
        total = self.total_by_extension[ext]

        best_category = max(category_counts, key=category_counts.get)
        confidence = category_counts[best_category] / total

        return best_category, confidence
