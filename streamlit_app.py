import streamlit as st
from agents.orchestrator import Orchestrator
from utils.pdf_utils import parse_pdf


orchestrator = Orchestrator()

# Streamlit App
st.title("Legal Agent Analyzer")
st.markdown("Upload a legal document (PDF) to analyze risks, summarize, and find relevant precedents.")

# File Upload
uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file:
    try:
        # Step 1: Parse the uploaded file
        st.info("Parsing the uploaded file...")
        document_text = parse_pdf(uploaded_file)
        st.success("File parsed successfully!")

        # Display parsed text (optional)
        if st.checkbox("Show Parsed Document Text"):
            st.text_area("Parsed Text", document_text, height=300)

        # Step 2: Analyze the contract
        st.info("Analyzing the document...")
        results = orchestrator.analyze_contract(document_text)
        st.success("Analysis Completed!")

        # Display Results
        st.subheader("Summary")
        st.write(results.get("summary", "No summary generated."))

        st.subheader("Risks")
        risks = results.get("risks", [])
        if isinstance(risks, list):
            for i, risk in enumerate(risks, 1):
                st.write(f"{i}. {risk}")
        else:
            st.write(risks)

        st.subheader("Precedents")
        precedents = results.get("precedents", [])
        if precedents:
            for i, precedent in enumerate(precedents, 1):
                st.write(f"{i}. {precedent}")
        else:
            st.write("No precedents found.")
    except Exception as e:
        st.error(f"An error occurred: {e}")