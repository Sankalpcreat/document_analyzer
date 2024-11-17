class RiskAgent:
    def __init__(self):
        pass

    def analyze_risk(self, summary):
        high_risk_keywords = ["penalty", "termination", "breach"]
        risk_score = sum(1 for word in high_risk_keywords if word in summary.lower())
        return {
            "summary": summary,
            "risk_score": min(risk_score * 3, 10) 
        }