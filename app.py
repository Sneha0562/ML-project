from mlProject.exception.exception_handler import AppException
import sys

try:
    a=3/0
except Exception as e:
    raise AppException(e,sys) from e    