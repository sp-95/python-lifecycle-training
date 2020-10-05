import os
from pathlib import Path

import pytest
import python_lifecycle
from pytest import fixture

from python_lifecycle_training import __version__


def test_version():
    assert __version__ == "0.1.0"
