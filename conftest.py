"""
Pytest fixtures for documentation testing.

DO NOT ADD OTHER FIXTURES HERE.
"""

import pytest


@pytest.fixture()
def my_fixture(tmp_path):
    """My_fixture example."""
    something = ...
    return something
