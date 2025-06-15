#can follow documentation as python exception documentation or 
#write 'custom exception handing documentation' (code as follows)

import sys
import logging
from typing import Any

def error_message_detail(error: Exception, error_detail: Any) -> str:
    _, _, exc_tb = error_detail
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error))
    return error_message

class CustomException(Exception):
    def __init__(self, error_message: str, error_detail: Any):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)  # Configure logging to see the log messages

    try:
        a = 1 / 0
    except Exception as e:
        logging.info("Divide by zero")
        raise CustomException(e, sys.exc_info())
