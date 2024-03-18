class SearchFromFile:
    """Class for opening a file and search through it."""
    def __init__(self) -> None:
        pass

    def open_file(self):
        """Opening a text file: """
        file_path = "test.txt"
        with open(file_path, "r") as fh:
            lines = fh.readlines()
            return lines
    
    def search_words(self, word):
        """Searching for words and/or phrases."""
        lines = self.open_file()
        return [line for line in lines if word in line]
    
if __name__ == "__main__":
    searcher = SearchFromFile()
    word = "your_search_word"  # replace with the word you want to search for
    lines_with_word = searcher.search_words(word)
    print(lines_with_word)
