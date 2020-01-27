from ffevaluation.home import home as __home
from ffevaluation.version import version as _version
import os
import logging.config

__version__ = _version()

try:
    logging.config.fileConfig(
        os.path.join(__home(), "logging.ini"), disable_existing_loggers=False
    )
except:
    print("FFEvaluation: Logging setup failed")
