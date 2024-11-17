import requests
import logging
from utils.embedding_utils import EmbeddingUtils

logger = logging.getLogger(__name__)

class CourtListenerAPI:
    def __init__(self, api_token, base_url="https://www.courtlistener.com/api/rest/v4/"):
        self.api_token = api_token
        self.base_url = base_url
        self.headers = {"Authorization": f"Token {api_token}"}
        self.embedding_utils = EmbeddingUtils()

    def search_opinions(self, query, page=1):
        """Search for legal opinions in CourtListener based on a query."""
        try:
            url = f"{self.base_url}opinions/"
            params = {"q": query, "page": page}
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching opinions: {e}")
            return {"error": str(e)}

    def search_with_embedding(self, text, page=1):
        """Generate embedding for text and use it to query CourtListener."""
        try:
            logger.info("Generating embedding for text query.")
            embedding = self.embedding_utils.generate_embedding(text)

            # Convert embedding into query-friendly text (e.g., keywords or phrases)
            query_text = " ".join([f"keyword{i}" for i, _ in enumerate(embedding[:5])])  # Example
            return self.search_opinions(query=query_text, page=page)
        except Exception as e:
            logger.error(f"Error performing embedding-driven search: {e}")
            return {"error": str(e)}