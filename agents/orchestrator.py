from workflows.summarization_workflow import get_summarization_workflow
from workflows.risk_workflow import get_risk_workflow
from workflows.precedent_workflow import get_precedent_workflow

class Orchestrator:
    def __init__(self):
        self.summarization_workflow = get_summarization_workflow()
        self.risk_workflow = get_risk_workflow()
        self.precedent_workflow = get_precedent_workflow()

    def analyze_contract(self, text):
        # Step 1: Summarize the document
        summary_output = self.summarization_workflow.invoke({"summary": text})
        summary = summary_output if isinstance(summary_output, str) else summary_output.get("summary", "No summary generated")

        # Step 2: Perform risk analysis
        risk_output = self.risk_workflow.invoke({"summary": summary})
        risks = risk_output if isinstance(risk_output, str) else risk_output.get("risks", "No risks identified")

        # Step 3: Search for precedents
        precedents_output = self.precedent_workflow.invoke({"summary": summary})
        precedents = precedents_output if isinstance(precedents_output, list) else []

        # Combine results
        return {
            "summary": summary,
            "risks": risks,
            "precedents": precedents
        }