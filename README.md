# AI Resume Screening System

An intelligent resume screening application that uses machine learning to match resumes against job descriptions and calculate similarity scores.

## Features

✨ **Key Features:**
- Upload and parse PDF resumes
- Enter job descriptions for comparison
- Calculate match scores using cosine similarity
- Visual feedback with color-coded results
- Extract and display resume text
- Progress indicators and error handling

## Project Structure

```
AI-Resume-Screening/
├── app.py              # Main Streamlit application
├── model.py            # ML model and matching logic
├── requirements.txt    # Python dependencies
├── resume.pdf          # Sample resume file
└── README.md           # This file
```

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup

1. Clone or download the project
```bash
cd AI-Resume-Screening
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

## Usage

Run the Streamlit application:
```bash
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

### Steps:
1. Upload a PDF resume
2. Paste the job description
3. Click "Screen Resume" button
4. View the match score and similarity analysis

<img width="1891" height="821" alt="Screenshot 2026-04-10 135103" src="https://github.com/user-attachments/assets/3d87b5ff-47de-45a8-8b3a-529cb57ef5b4" />


## How It Works

### Algorithm
- **Text Extraction:** PyPDF2 extracts text from PDF resumes
- **Vectorization:** CountVectorizer converts text to numerical vectors
- **Similarity:** Cosine similarity measures the angle between vectors
- **Scoring:** Results are normalized to 0-100 percentage scale

### Match Score Interpretation
- **80-100%:** ✅ Excellent match
- **60-79%:** ⚠️ Good match, may need review
- **Below 60%:** ❌ Poor match, consider other candidates

<img width="1812" height="852" alt="Screenshot 2026-04-10 135039" src="https://github.com/user-attachments/assets/77deb5e7-c148-4ea3-86ae-c5342eb3dc0e" />

## Dependencies

- **streamlit:** Web framework for the UI
- **PyPDF2:** PDF file processing
- **scikit-learn:** Machine learning and text vectorization
- **numpy:** Numerical computing
- **pandas:** Data manipulation

## Error Handling

The application includes robust error handling for:
- Invalid PDF files
- Missing file uploads
- Empty job descriptions
- PDF parsing errors

## Future Enhancements

- Multi-language support
- Advanced NLP with BERT/Transformers
- Resume ranking and filtering
- Batch processing
- Database integration
- Export results to CSV

## License

MIT License

## Support

For issues or questions, please check the error messages displayed in the application.

---

**Version:** 1.0  
**Last Updated:** 2026
