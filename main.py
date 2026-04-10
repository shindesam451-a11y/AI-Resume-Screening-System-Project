import streamlit as st
from model import screen_resume
import io

st.set_page_config(page_title="AI Resume Screening", layout="wide")

st.title("🤖 AI Resume Screening System")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📄 Upload Resume")
    uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")

with col2:
    st.subheader("📋 Job Description")
    job_desc = st.text_area("Paste Job Description", height=200)

st.markdown("---")

if st.button("🔍 Screen Resume", type="primary"):
    if not uploaded_file:
        st.error("❌ Please upload a resume PDF")
    elif not job_desc:
        st.error("❌ Please provide a job description")
    else:
        try:
            with st.spinner("Processing resume..."):
                # Convert uploaded file to BytesIO for processing
                uploaded_file.seek(0)
                match_score, resume_text = screen_resume(uploaded_file, job_desc)
            
            st.markdown("---")
            st.subheader("📊 Results")
            
            col1, col2 = st.columns([1, 2])
            with col1:
                # Display score with color coding
                if match_score >= 80:
                    st.success(f"✅ Match Score: **{match_score}%**")
                elif match_score >= 60:
                    st.warning(f"⚠️ Match Score: **{match_score}%**")
                else:
                    st.error(f"❌ Match Score: **{match_score}%**")
            
            with col2:
                # Progress bar
                st.progress(match_score / 100)
            
            st.markdown("---")
            st.subheader("📝 Extracted Resume Text")
            st.text_area("Resume Content:", value=resume_text, height=200, disabled=True)
            
        except Exception as e:
            st.error(f"Error processing resume: {str(e)}")