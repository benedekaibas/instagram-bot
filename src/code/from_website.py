import requests
from bs4 import BeautifulSoup

class SearchFromWebsite:
    """Class for scraping website."""
    def __init__(self) -> None:
        """Init function for the class."""
        pass

    def read_website(self):
        """Read data from the website."""
        url = "https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/"
        scrape = requests.get(url)
        content = BeautifulSoup(scrape.content, 'html.parser')
        return content

    def get_data_website(self):
        content = self.read_website()
        text = content.get_text()
        return text
        
# TODO: We should implement a function that removes blank lines since the text is full of blank lines.

    def blank_line(self):
        """Removing blank lines."""
        text_blank_lines = self.get_data_website()
        lines = text_blank_lines.split('\n')
        non_blank_lines = [line for line in lines if line.strip() != '']
        return '\n'.join(non_blank_lines)

if __name__ == "__main__":
    search = SearchFromWebsite()
    text_website = search.blank_line()
    print(text_website)
