import logging
import os
from workflows.summarization_workflow import get_summarization_workflow
from workflows.risk_workflow import get_risk_workflow
from workflows.precedent_workflow import get_precedent_workflow
from vector_store.populate_chroma import populate_chroma_store
from utils.court_listener_utils import CourtListenerAPI

logger = logging.getLogger(__name__)

class Orchestrator:
    def __init__(self):
        self.summarization_workflow = get_summarization_workflow()
        self.risk_workflow = get_risk_workflow()
        self.precedent_workflow = get_precedent_workflow()

        # Initialize CourtListener API using environment variables
        api_key = os.getenv("COURTLISTENER_API_KEY")
        if not api_key:
            logger.error("CourtListener API key is not set in environment variables.")
            raise EnvironmentError("CourtListener API key is missing.")

        self.court_listener_api = CourtListenerAPI(api_key)

    def setup_store(self, documents):
        logger.info("Setting up ChromaStore with provided documents.")
        populate_chroma_store(documents)

    def analyze_contract(self, text):
        try:
            # Step 1: Summarize the document
            logger.info("Starting document summarization.")
            summary_output = self.summarization_workflow.invoke({"summary": text})
            summary = summary_output if isinstance(summary_output, str) else summary_output.get("summary", "No summary generated")
            if not summary:
                logger.warning("No summary generated.")
                return {"error": "Summarization failed."}

            # Step 2: Analyze risks
            logger.info("Analyzing risks in the summary.")
            risk_output = self.risk_workflow.invoke({"summary": summary})
            risks = risk_output if isinstance(risk_output, str) else risk_output.get("risks", "No risks identified")

            # Step 3: Search precedents
            logger.info("Searching for precedents.")
            precedents_output = self.precedent_workflow.invoke({"summary": summary})
            precedents = precedents_output if isinstance(precedents_output, list) else []

            # Step 4: Search CourtListener for legal opinions
            logger.info("Searching CourtListener for legal opinions.")
            court_opinions = self.court_listener_api.search_opinions(query=summary)
            opinions = court_opinions.get("results", []) if "error" not in court_opinions else []

            # Combine results
            logger.info("Analysis completed successfully.")
            return {
                "summary": summary,
                "risks": risks,
                "precedents": precedents,
                "court_opinions": opinions,
            }
        except Exception as e:
            logger.error(f"Error in Orchestrator: {e}")
            return {"error": str(e)}