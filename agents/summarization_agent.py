import logging
from utils.api_utils import call_ollama
from utils.chunking_utils import chunk_text

logger = logging.getLogger(__name__)

def get_summarization_workflow():
    def summarization_workflow(text):
        try:
            logger.info("Starting text chunking for summarization.")
            chunks = chunk_text(text)
            summaries = []

            for chunk in chunks:
                logger.info("Requesting summary for a chunk.")
                summary = call_ollama(prompt=f"Summarize this legal text:\n{chunk}")
                summaries.append(summary)

            return " ".join(summaries)
        except Exception as e:
            logger.error(f"Error in summarization workflow: {e}")
            return "Error: Unable to summarize the document."
    return summarization_workflow