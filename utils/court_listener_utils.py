import requests
import logging

logger = logging.getLogger(__name__)

class CourtListenerAPI:
    def __init__(self, api_token):
        self.base_url = "https://www.courtlistener.com/api/rest/v4/"
        self.headers = {"Authorization": f"Token {api_token}"}

    def search_opinions(self, query, page=1):
        """Search for legal opinions in CourtListener."""
        try:
            url = f"{self.base_url}opinions/"
            params = {"q": query, "page": page}
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching opinions: {e}")
            return {"error": str(e)}