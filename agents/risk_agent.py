import logging

logger = logging.getLogger(__name__)

class RiskAgent:
    def __init__(self):
        self.high_risk_keywords = ["penalty", "termination", "breach"]

    def analyze_risk(self, summary):
        try:
            logger.info("Analyzing risks in the summary.")
            risk_score = sum(1 for word in self.high_risk_keywords if word in summary.lower())

            logger.info(f"Risk score calculated: {risk_score}.")
            return {
                "summary": summary,
                "risk_score": min(risk_score * 3, 10) 
            }
        except Exception as e:
            logger.error(f"Error during risk analysis: {e}")
            return {"error": str(e)}