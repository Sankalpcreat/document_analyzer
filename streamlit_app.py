from dotenv import load_dotenv
import os
import streamlit as st
from agents.orchestrator import Orchestrator
from utils.pdf_utils import parse_pdf
from utils.embedding_utils import EmbeddingUtils
from vector_store.chroma_store import ChromaStore
from utils.court_listener_utils import CourtListenerAPI

# Load environment variables
load_dotenv()

# Initialize components
orchestrator = Orchestrator()
embedding_utils = EmbeddingUtils()
chroma_store = ChromaStore()

# Retrieve CourtListener API configuration
court_listener_api_key = os.getenv("COURTLISTENER_API_KEY")
court_listener_base_url = os.getenv("COURTLISTENER_API_BASE_URL", "https://www.courtlistener.com/api/rest/v4/")

# Ensure API key is set
if not court_listener_api_key:
    st.error("CourtListener API key is not set. Please configure it in the environment file.")
    st.stop()

court_listener_api = CourtListenerAPI(api_token=court_listener_api_key, base_url=court_listener_base_url)

# Streamlit App
st.title("Legal Agent Analyzer")
st.markdown("Upload a legal document (PDF) to analyze risks, summarize, find relevant precedents, and perform semantic searches.")

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

        # Display Analysis Results
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

        # Step 3: Generate Embedding for Semantic Search
        st.info("Generating embedding for semantic search...")
        embedding = embedding_utils.generate_embedding(document_text)
        st.success("Embedding generated successfully!")

        # Step 4: Semantic Search in ChromaDB
        st.info("Searching for semantically similar documents in ChromaDB...")
        search_results = chroma_store.search(embedding, top_k=5)
        st.success("Semantic search in ChromaDB completed!")

        # Display Semantic Search Results
        st.subheader("Semantic Search Results (ChromaDB)")
        search_ids = search_results.get("ids", [])
        search_metadata = search_results.get("metadatas", [])

        if search_ids:
            for i, (doc_id, metadata) in enumerate(zip(search_ids[0], search_metadata[0]), 1):
                st.write(f"{i}. Document ID: {doc_id}")
                if metadata:
                    st.write(f"   Metadata: {metadata}")
        else:
            st.write("No similar documents found in ChromaDB.")

        # Step 5: Semantic Search with CourtListener
        st.info("Performing semantic search on CourtListener using generated embeddings...")
        court_opinions = court_listener_api.search_with_embedding(text=document_text)
        st.success("Semantic search with CourtListener completed!")

        # Display CourtListener Results
        st.subheader("Legal Opinions (CourtListener)")
        opinions = court_opinions.get("results", [])
        if opinions:
            for i, opinion in enumerate(opinions, 1):
                st.write(f"{i}. {opinion.get('caseName', 'Unknown Case')} - [View Opinion]({opinion.get('absolute_url', '#')})")
        else:
            st.write("No legal opinions found on CourtListener.")

    except Exception as e:
        st.error(f"An error occurred: {e}")