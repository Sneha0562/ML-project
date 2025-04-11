import sys
import os

# Add 'src' directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
from mlProject.exception.exception_handler import AppException
import sys
from mlProject.logger.log import logging

try:
    a=3/0
except Exception as e:
    raise AppException(e,sys) from e  

    loggig.info(e)
    raise AppException(e,sys) from e 