import os
from pathlib import Path

import pytest
import python_lifecycle_training
from pytest import fixture

from python_lifecycle_training import __version__


def test_version() -> None:
    assert __version__ == "0.1.0"
