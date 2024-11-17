import logging
from agents.orchestrator import Orchestrator
from utils.pdf_utils import parse_pdf
from config.logging_config import configure_logging

# Configure logging
logger = configure_logging()

def main():
    logger.info("Starting Legal AI Analyzer Application...")

    # Step 1: Load and parse the input file
    file_path = input("Enter the path to the legal document (PDF): ").strip()
    try:
        logger.info(f"Parsing file: {file_path}")
        document_text = parse_pdf(file_path)
        logger.info("File parsed successfully.")
    except Exception as e:
        logger.error(f"Error parsing file: {e}")
        print("Failed to parse the file. Please check the file path and try again.")
        return

    # Step 2: Initialize the Orchestrator
    logger.info("Initializing Orchestrator...")
    orchestrator = Orchestrator()

    # Step 3: Analyze the contract
    try:
        logger.info("Analyzing the contract...")
        results = orchestrator.analyze_contract(document_text)
        logger.info("Contract analysis completed.")
    except Exception as e:
        logger.error(f"Error during analysis: {e}")
        print("An error occurred during contract analysis. Please check the logs.")
        return

    # Step 4: Display the results
    logger.info("Displaying results...")
    print("\n--- Analysis Results ---")

    # Display Summary
    print("\nSummary:")
    if "error" in results:
        print(f"Error: {results['error']}")
    else:
        print(results["summary"])

    # Display Risks
    print("\nRisks:")
    risks = results.get("risks", [])
    if isinstance(risks, str):
        print(risks)
    else:
        for i, risk in enumerate(risks, start=1):
            print(f"{i}. {risk}")

    # Display Precedents
    print("\nPrecedents:")
    precedents = results.get("precedents", [])
    if not precedents:
        print("No precedents found.")
    else:
        for i, precedent in enumerate(precedents, start=1):
            print(f"{i}. {precedent}")

    logger.info("Results displayed successfully.")

if __name__ == "__main__":
    main()