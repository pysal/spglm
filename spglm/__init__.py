import contextlib
from importlib.metadata import PackageNotFoundError, version

from . import (
    family,
    glm,
    iwls,
    utils,
)

with contextlib.suppress(PackageNotFoundError):
    __version__ = version("spglm")
