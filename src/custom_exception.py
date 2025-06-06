import traceback
import sys

class CustomException(Exception):
    def __init__(self, error_message):
        super().__init__(error_message)
        self.error_message = self.get_detailed_error_message(error_message)

    @staticmethod
    def get_detailed_error_message(error_message):
        _, _, exc_tb = traceback.sys.exc_info()
        if exc_tb is not None:
            line_number = exc_tb.tb_frame.f_lineno
            file_name = exc_tb.tb_frame.f_code.co_filename
            return f"Error occurred in script: [{file_name}] at line number: [{line_number}] error message: [{error_message}]"
        else:
            return error_message
    
    def __str__(self):
        return self.error_message

    
   