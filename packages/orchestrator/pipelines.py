from pathlib import Path
from datetime import datetime

from .actions import log
from .guardrails import safe_execute

TRIAGE_PROMPT_PATH = Path("packages/templates/TRIAGE_PROMPT.md")


def triage() -> None:
    prompt = TRIAGE_PROMPT_PATH.read_text(encoding="utf-8")
    date_str = datetime.now().strftime("%Y-%m-%d")
    report_path = Path(f"docs/triage/D-{date_str}.md")
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(f"# Triage Report ({date_str})\n\n{prompt}\n", encoding="utf-8")
    log(f"Триаж завершён. Отчёт: {report_path}")


if __name__ == "__main__":
    safe_execute(triage)
