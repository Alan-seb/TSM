import re

PATTERN = re.compile(
    r"logs\s+of\s+(\d+)\s+(minutes|hours|days)\s+ago",
    re.IGNORECASE
)

def parse_text(text: str) -> dict:
    match = PATTERN.search(text)
    if not match:
        raise ValueError("Unsupported query")

    value, unit = match.groups()

    return {
        "type": "journal_query",
        "time": {"value": int(value), "unit": unit},
        "service": None,
        "priority": None,
        "kernel": False
    }