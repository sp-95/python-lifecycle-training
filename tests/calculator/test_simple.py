import os
from pathlib import Path

import pytest
from pytest import fixture

import python_lifecycle_training
from python_lifecycle_training import __version__


def test_version():
    assert __version__ == "0.1.0"
