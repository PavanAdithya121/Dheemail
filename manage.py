#!/usr/bin/env python
"""Top-level wrapper to make the inner Django project importable for hosts.

This file ensures the `dheemail/` package (the inner project folder) is on
`sys.path` so imports like `dheemail.settings` work when the host runs from the
repository root (for example, Vercel builds).
"""
import os
import sys


BASE_DIR = os.path.dirname(__file__)
# Ensure the project root is searched first so the real `mailapp` app is imported.
sys.path.insert(0, BASE_DIR)
# Add the inner project folder to sys.path so `import dheemail` succeeds.
sys.path.insert(1, os.path.join(BASE_DIR, "dheemail"))


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dheemail.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Is it installed and available on your "
            "PYTHONPATH? Did you forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
