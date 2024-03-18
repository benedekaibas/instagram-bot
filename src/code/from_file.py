class SearchFromFile:
    """Class for opening a file and search through it."""

    def open_file():
        """Opening a text file: """
        with open(file_path, "w") as fh:
            for url in telex_url:
                fh.write(f"{url}\n")