from python_lifecycle_training import __version__
import python_lifecycle
from pytest import fixture
import pytest
import os
from pathlib import Path


def test_version():
    assert __version__ == '0.1.0'
