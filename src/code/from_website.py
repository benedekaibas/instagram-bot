
import requests

class SearchFromWebsite:
    """Class for scraping website."""
    def __init__(self) -> None:
        """Init function for the class."""
        pass

    def read_website(self):
        url = "https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/"
        scrape = requests.get(url)
        content = scrape.content
        return content
    
if __name__ == "__main__":
    search = SearchFromWebsite()
    website_content = search.read_website()
    print(website_content)