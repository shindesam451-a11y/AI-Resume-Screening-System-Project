# 🤖 AI Resume Screening System

## 📌 Project Overview

The AI Resume Screening System is a machine learning-based application that automates the process of evaluating resumes against job descriptions. It uses Natural Language Processing (NLP) techniques to analyze resume content and match it with required skills, providing a similarity score and actionable insights.

---

## 🎯 Objective

To build an intelligent system that helps recruiters and organizations efficiently shortlist candidates by comparing resumes with job requirements and identifying the best matches.

---

## 🚀 Features

* 📄 Upload resume in PDF format
* 📝 Input job description
* 📊 Calculate match score using cosine similarity
* 🔍 Identify missing skills and keywords
* 📈 Highlight matched skills
* 💻 Interactive user interface using Streamlit

---

## 🛠️ Tech Stack

* **Programming Language:** Python
* **Libraries:** Pandas, Scikit-learn, NLTK / spaCy, PyPDF2
* **Visualization/UI:** Streamlit
* **Concepts Used:** NLP, Text Vectorization (CountVectorizer / TF-IDF), Cosine Similarity

---

## ⚙️ How It Works

1. Extract text from uploaded resume (PDF)
2. Clean and preprocess text data
3. Convert resume and job description into numerical vectors
4. Compute similarity using cosine similarity
5. Display match score and skill comparison
<img width="1891" height="821" alt="Screenshot 2026-04-10 135103" src="https://github.com/user-attachments/assets/d49d831e-259b-454c-baad-dfbf084aad8b" />

---

## 📊 Output

* Match Score (%) between resume and job description
* List of matched skills
* List of missing skills
<img width="1812" height="852" alt="Screenshot 2026-04-10 135039" src="https://github.com/user-attachments/assets/b61eb3b2-5dd2-4add-b7db-de32be17521b" />

---

## 💡 Future Enhancements

* Use advanced NLP models (BERT / Transformers)
* Improve skill extraction using Named Entity Recognition (NER)
* Deploy application on cloud (AWS / Heroku)
* Add multiple resume comparison feature

---

## 📂 Project Structure

```
AI-Resume-Screening/
│── app.py
│── model.py
│── resume.pdf
│── requirements.txt
│── README.md
```

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 🎤 Use Case

This project can be used by HR professionals and recruiters to automate resume screening, reduce manual effort, and improve hiring efficiency.

---

## 🙌 Acknowledgment

This project is built as part of a data science learning journey to apply real-world machine learning and NLP concepts.

---
