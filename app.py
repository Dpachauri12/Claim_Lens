import streamlit as st
import pandas as pd
import tempfile

from utils.styles import custom_css
from utils.pdf_extractor import extract_text_from_pdf
from utils.claim_detector import extract_claims
from utils.verifier import verify_claim
from utils.report_generator import generate_report

st.set_page_config(
    page_title="GEO Truth Engine",
    layout="wide"
)

st.markdown(custom_css, unsafe_allow_html=True)

st.title("GEO Truth Engine")
st.caption("AI Visibility Intelligence & Fact Verification Platform")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("ChatGPT Visibility", "82%")

with col2:
    st.metric("Gemini Visibility", "74%")

with col3:
    st.metric("Hallucination Risk", "21%")

st.divider()

uploaded_file = st.file_uploader(
    "Upload Marketing PDF",
    type=["pdf"]
)

if uploaded_file:

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        pdf_path = tmp_file.name

    with st.spinner("Analyzing PDF and verifying claims..."):

        text = extract_text_from_pdf(pdf_path)
        claims = extract_claims(text)

        results = []

        for claim in claims:
            verification = verify_claim(claim)

            results.append({
                "claim": claim,
                "status": verification["status"],
                "correct_fact": verification["correct_fact"],
                "source": verification["source"],
                "confidence": verification["confidence"]
            })

    st.success("Verification completed")

    df = pd.DataFrame(results)

    st.dataframe(df, use_container_width=True)

    report_path = generate_report(results)

    with open(report_path, "rb") as file:
        st.download_button(
            label="Download Verification Report",
            data=file,
            file_name="verification_report.pdf",
            mime="application/pdf"
        )