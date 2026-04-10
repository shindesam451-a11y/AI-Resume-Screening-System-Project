from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import io

# Function to extract text from PDF
def extract_text_from_pdf(file):
    """Extract text from PDF file"""
    try:
        pdf_reader = PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        raise ValueError(f"Error reading PDF: {str(e)}")

# Function to calculate match score
def calculate_match_score(resume_text, job_description):
    """
    Calculate similarity score between resume and job description
    Returns score from 0-100
    """
    try:
        if not resume_text or not job_description:
            return 0
        
        # Convert text to vectors
        cv = CountVectorizer()
        vectors = cv.fit_transform([resume_text, job_description])
        
        # Calculate cosine similarity
        similarity = cosine_similarity(vectors)[0][1]
        
        return round(similarity * 100, 2)
    except Exception as e:
        raise ValueError(f"Error calculating match score: {str(e)}")

# Function for combined pipeline
def screen_resume(pdf_file, job_description):
    """
    Main screening function
    Returns match score and extracted resume text
    """
    resume_text = extract_text_from_pdf(pdf_file)
    match_score = calculate_match_score(resume_text, job_description)
    return match_score, resume_text
