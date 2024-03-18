class SearchFromFile:
    """Class for opening a file and search through it."""
    def __init__(self) -> None:
        pass

    def open_file(self):
        """Opening a text file: """
        file_path = "test.txt"
        with open(file_path, "r") as fh:
            lines = fh.readlines()
            lines_lower_case = [line.lower() for line in lines]
            return lines_lower_case
    
    def search_words(self, word):
        """Searching for words and/or phrases."""
        lines = self.open_file()
        return [line for line in lines if word in line]
    
    def user_input(self):
        user_input = str(input("enter your word: "))
        return user_input
    
if __name__ == "__main__":
    searcher = SearchFromFile()
    word = searcher.user_input() # replace with the word you want to search for
    lines_with_word = searcher.search_words(word)
    print(lines_with_word)
