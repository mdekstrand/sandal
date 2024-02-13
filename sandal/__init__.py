"""
Lightweight bootstrapping for project scripts
"""

from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("sandal")
except PackageNotFoundError:
    # package is not installed
    pass
