# This is an optional dependency, so importing
# _this_ package will fail if you don't have it
from rich import print as rprint


def remove_arrow():
    # Uses the rich library for formatting
    rprint("[italic red]It's stuck! Can't remove[/italic red]")
    raise SystemExit(1)
