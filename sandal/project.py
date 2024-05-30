"""
Utility code for managing projects.
"""

# pyright: basic
import os
import sys
from pathlib import Path

from pyprojroot import find_root, has_dir, here

__all__ = ["here", "setup_project_dir"]

_root_dir: Path


def setup_project_dir():
    global _root_dir
    _root_dir = find_root(has_dir(".git"))
    sys.path.insert(0, os.fspath(_root_dir))
