ALLOWED_TIME_UNITS = {"minutes", "hours", "days"}
ALLOWED_PRIORITIES = {0, 1, 2, 3, 4, 5, 6, 7}

def build_journalctl_command(intent: dict) -> str:
    if intent.get("type") != "journal_query":
        raise ValueError("Invalid intent type")

    time = intent.get("time")
    if not time:
        raise ValueError("Time is required")

    value = time.get("value")
    unit = time.get("unit")

    if not isinstance(value, int) or value <= 0:
        raise ValueError("Invalid time value")

    if unit not in ALLOWED_TIME_UNITS:
        raise ValueError("Invalid time unit")

    cmd = ["journalctl"]

    # Kernel logs only
    if intent.get("kernel"):
        cmd.append("-k")

    # Service filter
    service = intent.get("service")
    if service:
        if not service.isidentifier():
            raise ValueError("Invalid service name")
        cmd.extend(["-u", service])

    # Priority filter
    priority = intent.get("priority")
    if priority is not None:
        if priority not in ALLOWED_PRIORITIES:
            raise ValueError("Invalid priority")
        cmd.extend(["-p", str(priority)])

    cmd.extend([
        "--since",
        f"{value} {unit} ago",
        "--no-pager"
    ])

    return " ".join(cmd)