import sys

def error_message_detail(error, error_detail:sys):
    '''
    function to extract detailed information about an error, 
    including the filename and line number where the error occurred
    '''
    # Get the traceback object from the error details
    _, _, exc_tb = error_detail.exc_info()
    
    # Get the filename where the error occurred
    file_name = exc_tb.tb_frame.f_code.co_filename
    
    # Create an error message with the filename, line number, and error message
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    '''
    Defines a custom exception class that inherits from the built-in Exception class
    '''
    def __init__(self, error_message, error_detail:sys):
        
        # Initialize the parent class with the error message
        super().__init__(error_message)
        
        # Store the detailed error message
        self.error_message = error_message_detail(error_message, error_detail)
        
    def __str__(self):
        # Return the detailed error message when the exception is printed
        return self.error_message
