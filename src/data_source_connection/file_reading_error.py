"""
This Module defines the possible errors while using the file reading utility
"""


class FileReadingError(Exception):
    def __init__(self):
        pass


class FileNotFound(FileReadingError):
    def __init__(self):
        pass


class ZeroDataFrame(FileReadingError):
    def __init__(self):
        pass
