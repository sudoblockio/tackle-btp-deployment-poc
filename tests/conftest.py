import os
import pytest


@pytest.fixture(scope='function')
def chdir(request):
    """Change to a directory based on an argument within the scope of the test."""

    def f(dir):
        os.chdir(os.path.join(request.fspath.dirname, dir))

    return f


@pytest.fixture(scope='function')
def change_base_dir(monkeypatch):
    """Change to the base directory for importing hooks."""
    monkeypatch.chdir(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..'))


@pytest.fixture(scope='function')
def hooks_dir(change_base_dir):
    """Get a string location to the hooks dir."""
    return os.path.abspath('.hooks')
