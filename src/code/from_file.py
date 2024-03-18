class SearchFromFile:
    """Class for opening a file and search through it."""

    def open_file():
        """Opening a text file: """
        file_path = "test.txt"
        with open(file_path, "r") as fh:
            lines = fh.readlines()
            return lines