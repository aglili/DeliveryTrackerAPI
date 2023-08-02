class TrackerError(Exception):
    """
    There is an error
    """

class InvalidNumber(TrackerError):
    """
    The Number You Passed is Incorrect
    """