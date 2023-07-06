import shutil
import tempfile
from typing import Any


def create_temp_dir() -> tempfile.TemporaryDirectory[str]:
    return tempfile.TemporaryDirectory()


def remove_temp_dir(temp_dir: tempfile.TemporaryDirectory[Any] | str) -> None:
    if isinstance(temp_dir, str):
        shutil.rmtree(temp_dir, ignore_errors=True)
    else:
        temp_dir.cleanup()
