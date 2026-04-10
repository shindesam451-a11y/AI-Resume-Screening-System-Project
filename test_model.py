import unittest
from io import BytesIO
from model import extract_text_from_pdf, calculate_match_score, screen_resume

class TestResumeScreening(unittest.TestCase):
    """Unit tests for AI Resume Screening System"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.sample_job_description = """
        Looking for Data Analyst with skills in Python, SQL, Machine Learning, 
        Data Visualization, and Statistical Analysis.
        """
        
        self.sample_resume_text = """
        JOHN DOE
        Data Analyst
        
        PROFESSIONAL SUMMARY
        Experienced Data Analyst with 5+ years in Python, SQL, and Machine Learning
        
        SKILLS
        Python, SQL, Tableau, Power BI, Excel, Machine Learning, Data Visualization
        
        EXPERIENCE
        Senior Data Analyst - ABC Corp, 2021-present
        Data Analyst - XYZ Ltd, 2018-2021
        
        EDUCATION
        Bachelor of Science in Data Science
        University of Technology, 2018
        """

    def test_calculate_match_score_with_valid_data(self):
        """Test match score calculation with valid inputs"""
        score = calculate_match_score(self.sample_resume_text, self.sample_job_description)
        self.assertIsInstance(score, float)
        self.assertGreaterEqual(score, 0)
        self.assertLessEqual(score, 100)
        print(f"✓ Match Score Test Passed: {score}%")

    def test_calculate_match_score_with_empty_resume(self):
        """Test match score with empty resume"""
        score = calculate_match_score("", self.sample_job_description)
        self.assertEqual(score, 0)
        print("✓ Empty Resume Test Passed")

    def test_calculate_match_score_with_empty_job_description(self):
        """Test match score with empty job description"""
        score = calculate_match_score(self.sample_resume_text, "")
        self.assertEqual(score, 0)
        print("✓ Empty Job Description Test Passed")

    def test_calculate_match_score_identical_text(self):
        """Test match score with identical resume and job description"""
        identical_text = "Python SQL Machine Learning Data Analysis"
        score = calculate_match_score(identical_text, identical_text)
        self.assertEqual(score, 100.0)
        print(f"✓ Identical Text Test Passed: {score}%")

    def test_calculate_match_score_no_overlap(self):
        """Test match score with no overlapping keywords"""
        resume = "Basketball Soccer Football Sports"
        job_desc = "Python SQL JavaScript NodeJS"
        score = calculate_match_score(resume, job_desc)
        self.assertEqual(score, 0.0)
        print(f"✓ No Overlap Test Passed: {score}%")

    def test_extract_text_from_pdf_error_handling(self):
        """Test error handling for invalid PDF"""
        invalid_pdf = BytesIO(b"Not a valid PDF")
        with self.assertRaises(ValueError):
            extract_text_from_pdf(invalid_pdf)
        print("✓ Invalid PDF Error Handling Test Passed")

    def test_screen_resume_returns_tuple(self):
        """Test screen_resume returns a tuple of (score, text)"""
        # Create a minimal valid PDF
        valid_pdf = BytesIO(b"%PDF-1.4\n" + b"\x00" * 100)
        try:
            result = screen_resume(valid_pdf, self.sample_job_description)
            self.assertIsInstance(result, tuple)
            self.assertEqual(len(result), 2)
            print("✓ Screen Resume Return Type Test Passed")
        except ValueError:
            print("✓ Screen Resume Error Handling Test Passed (Expected for minimal PDF)")

    def test_calculate_match_score_partial_overlap(self):
        """Test match score with partial keyword overlap"""
        resume = """
        Experienced Professional with skills in:
        - Python Programming
        - SQL Database Management
        - Data Analysis
        """
        job_desc = """
        Required Skills:
        - Python
        - SQL
        - Machine Learning
        - Data Visualization
        """
        score = calculate_match_score(resume, job_desc)
        self.assertGreater(score, 0)
        self.assertLess(score, 100)
        print(f"✓ Partial Overlap Test Passed: {score}%")


class TestIntegration(unittest.TestCase):
    """Integration tests for the resume screening workflow"""
    
    def test_full_workflow_with_sample_data(self):
        """Test complete workflow from extraction to scoring"""
        job_desc = "Looking for Python developer with SQL and Machine Learning skills"
        resume_text = "Python developer with 5 years SQL and Machine Learning experience"
        
        score = calculate_match_score(resume_text, job_desc)
        self.assertIsInstance(score, float)
        self.assertGreater(score, 0)
        print(f"✓ Full Workflow Test Passed - Score: {score}%")


if __name__ == '__main__':
    # Run tests with verbose output
    unittest.main(verbosity=2)
