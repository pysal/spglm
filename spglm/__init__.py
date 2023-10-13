import contextlib
from importlib.metadata import PackageNotFoundError, version

from . import glm  # noqa F401
from . import family  # noqa F401
from . import utils  # noqa F401
from . import iwls  # noqa F401

with contextlib.suppress(PackageNotFoundError):
    __version__ = version("spglm")