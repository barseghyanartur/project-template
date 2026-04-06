"""
Pytest fixtures for documentation testing.

DO NOT ADD OTHER FIXTURES HERE.
"""

import pytest


@pytest.fixture()
def my_fixture(tmp_path):
    """My_fixture example."""
    # TODO: mock stuff, do other things that your tests need to run properly
    something = "some value"
    return something
