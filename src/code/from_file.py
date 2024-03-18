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
        """Getting user input."""
        user_input = str(input("enter your word: "))
        return user_input
    
    def highlight_word(self):
        """Highlighting word that the user inputs."""
        word = self.user_input()
        lines = self.open_file()
        highlighted_lines = []
        for line in lines:
            highlighted_line = line.replace(word, f"\033[1;31;40m{word}\033[0m")
            highlighted_lines.append(highlighted_line)
        return highlighted_lines

    def count_words(self):
        """Counting the searched words."""
        return 0


if __name__ == "__main__":
    searcher = SearchFromFile()
    highlighted_lines = searcher.highlight_word()
    print('\n'.join(highlighted_lines))
