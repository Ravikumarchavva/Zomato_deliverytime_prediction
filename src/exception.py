import traceback

class ZomatoException(Exception):
    """
    Custom exception class for the Zomato project.
    Captures the error message and optional stack trace.
    """

    def __init__(self, message: str, original_exception: Exception = None):
        """
        :param message: Custom error message for the exception.
        :param original_exception: The original exception object, if any.
        """
        self.message = message
        self.original_exception = original_exception
        super().__init__(self.message)

    def __str__(self):
        if self.original_exception:
            return f"{self.message} | Original Exception: {str(self.original_exception)}"
        return self.message

    def log_error(self):
        """
        Logs the error message and stack trace for debugging.
        """
        error_details = f"Error: {self.message}\n"
        if self.original_exception:
            error_details += f"Original Exception: {traceback.format_exc()}"
        print(error_details)


if __name__ == "__main__":
    try:
        raise ZomatoException("This is a custom exception.")
    except ZomatoException as e:
        e.log_error()