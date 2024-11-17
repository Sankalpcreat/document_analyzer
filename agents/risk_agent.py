import logging

logger = logging.getLogger(__name__)

def get_risk_workflow():
    def risk_workflow(summary):
        try:
            logger.info("Analyzing risks in the provided summary.")
            high_risk_keywords = ["penalty", "termination", "breach"]
            risk_score = sum(1 for word in high_risk_keywords if word in summary.lower())
            logger.info(f"Risk analysis completed with score: {risk_score}.")
            return {
                "summary": summary,
                "risk_score": min(risk_score * 3, 10)
            }
        except Exception as e:
            logger.error(f"Error in risk workflow: {e}")
            return {"error": str(e)}
    return risk_workflow