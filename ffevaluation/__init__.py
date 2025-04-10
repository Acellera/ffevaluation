import os
import logging.config
from importlib.metadata import version, PackageNotFoundError

# from importlib.resources import files

try:
    __version__ = version("ffevaluation")
except PackageNotFoundError:
    pass

__curr_dir = os.path.dirname(os.path.abspath(__file__))
try:
    logging.config.fileConfig(
        os.path.join(__curr_dir, "logging.ini"), disable_existing_loggers=False
    )
except Exception:
    print("FFEvaluation: Logging setup failed")
