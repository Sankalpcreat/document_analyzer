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
    try:
        orchestrator = Orchestrator()
    except Exception as e:
        logger.error(f"Error initializing Orchestrator: {e}")
        print("An error occurred during Orchestrator initialization. Please check the logs.")
        return

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
    try:
        logger.info("Displaying results...")
        print("\n--- Analysis Results ---")

        print("\nSummaries:")
        summaries = results.get("summary", [])
        if summaries:
            for i, summary in enumerate(summaries, start=1):
                print(f"{i}. {summary}")
        else:
            print("No summaries available.")

        print("\nRisks:")
        risks = results.get("risks", [])
        if risks:
            for i, risk in enumerate(risks, start=1):
                print(f"{i}. {risk}")
        else:
            print("No risks identified.")

        print("\nPrecedents:")
        precedents = results.get("precedents", [])
        if precedents:
            for i, precedent in enumerate(precedents, start=1):
                print(f"{i}. {precedent}")
        else:
            print("No precedents found.")

        logger.info("Results displayed successfully.")

    except Exception as e:
        logger.error(f"Error displaying results: {e}")
        print("An error occurred while displaying results. Please check the logs.")
        return


if __name__ == "__main__":
    main()