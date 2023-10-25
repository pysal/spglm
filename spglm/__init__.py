import contextlib
from importlib.metadata import PackageNotFoundError, version

from . import (
    family,  # noqa F401
    glm,  # noqa F401
    iwls,  # noqa F401
    utils,  # noqa F401
)

with contextlib.suppress(PackageNotFoundError):
    __version__ = version("spglm")
