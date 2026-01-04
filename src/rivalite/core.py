"""
Core utilities for the library Rivalite

These core utilities support the rest of the library. The functions here are designed for quick and easy optimizations for your code.
"""

from pathlib import Path

def ensure_list(value):
    """
    Returns the value as a list even if it isn't iterable

    - If the value is None, it returns an empty list.
    - If the value is a list; tuple; or set, it returns the data as a list
    - Otherwise, it wraps the value in a list
    """

    if value is None:
        return []

    if isinstance(value, (list, tuple, set)):
        return list(value)

    else:
        return [value]

def about():
    """
    Returns a list of all available modules
    """

    package_dir = Path(__file__).parent
    files = [p.name for p in package_dir.iterdir()]
    for f in files[:]:
        if f.startswith("_"):
            files.remove(f)
    for i, f in enumerate(files):
        files[i] = f[:-3]
    return files

