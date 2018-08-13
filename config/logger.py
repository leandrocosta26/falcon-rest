import logging
import os
import sys

SYSTEM_OUT = logging.StreamHandler(sys.stdout)

SYSTEM_OUT.setLevel(logging.INFO)

FORMATTER = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(filename)s - %(funcName)s - %(message)s')

SYSTEM_OUT.setFormatter(FORMATTER)

logger = logging.getLogger("Falcon")

logger.setLevel(logging.INFO)

logger.addHandler(SYSTEM_OUT)
