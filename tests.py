from tjct import build_journalctl_command

def test_basic_time_query():
    intent = {
        "type": "journal_query",
        "time": {"value": 2, "unit": "hours"},
        "service": None,
        "priority": None,
        "kernel": False
    }

    cmd = build_journalctl_command(intent)
    assert cmd == 'journalctl --since "2 hours ago" --no-pager'


def test_kernel_priority_query():
    intent = {
        "type": "journal_query",
        "time": {"value": 30, "unit": "minutes"},
        "kernel": True,
        "priority": 3,
        "service": None
    }

    cmd = build_journalctl_command(intent)
    assert cmd == 'journalctl -k -p 3 --since "30 minutes ago" --no-pager'


def test_service_query():
    intent = {
        "type": "journal_query",
        "time": {"value": 1, "unit": "days"},
        "service": "ssh",
        "priority": None,
        "kernel": False
    }

    cmd = build_journalctl_command(intent)
    assert cmd == 'journalctl -u ssh --since "1 days ago" --no-pager'


def test_invalid_time_unit():
    intent = {
        "type": "journal_query",
        "time": {"value": 5, "unit": "weeks"},
        "service": None,
        "priority": None,
        "kernel": False
    }

    try:
        build_journalctl_command(intent)
        assert False, "Expected ValueError"
    except ValueError:
        pass


def test_negative_time():
    intent = {
        "type": "journal_query",
        "time": {"value": -1, "unit": "hours"},
        "service": None,
        "priority": None,
        "kernel": False
    }

    try:
        build_journalctl_command(intent)
        assert False, "Expected ValueError"
    except ValueError:
        pass


def test_command_injection_attempt():
    intent = {
        "type": "journal_query",
        "time": {"value": 1, "unit": "hours"},
        "service": "ssh; rm -rf /",
        "priority": None,
        "kernel": False
    }

    try:
        build_journalctl_command(intent)
        assert False, "Expected ValueError"
    except ValueError:
        pass