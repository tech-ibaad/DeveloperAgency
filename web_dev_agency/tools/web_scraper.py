import requests
from bs4 import BeautifulSoup
from agency_swarm.tools import BaseTool
from pydantic import Field

class WebScraper(BaseTool):
    url: str = Field(..., description="The URL to scrape")

    def run(self):
        try:
            response = requests.get(self.url, headers={"User-Agent": "Mozilla/5.0"})
            soup = BeautifulSoup(response.text, "html.parser")
            return soup.get_text()[:1000]
        except Exception as e:
            return f"Error: {str(e)}"
