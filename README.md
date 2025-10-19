# ResumeAI - Smart Resume Analyzer

AI-powered resume optimization tool that helps job seekers get past Applicant Tracking Systems using Natural Language Processing and Machine Learning.

---

## Problem Statement

Job seekers face significant challenges in today's competitive market. Over 70% of resumes are rejected by Applicant Tracking Systems (ATS) before reaching human recruiters. Candidates lack visibility into why their resumes are rejected and struggle to identify missing keywords that match job requirements. There are no accessible tools that provide instant, actionable resume feedback.

ResumeAI addresses this problem by providing AI-powered analysis that helps candidates optimize their resumes, identify skill gaps, and improve their chances of landing interviews.

---

## Tech Stack

### Backend
- Python 3.12
- Flask 3.0.3 - Web framework for REST API
- HuggingFace Transformers 4.45.2 - AI model integration
- PyTorch 2.4.1 - Deep learning framework
- Google FLAN-T5-Large - 780M parameter language model
- Flask-CORS 5.0.0 - Cross-origin resource sharing

### Frontend
- HTML5, CSS3, JavaScript ES6+
- Tailwind CSS 3.4 - Utility-first styling framework
- Feather Icons - Icon library
- Responsive design for mobile and desktop

### NLP and AI
- Text-to-Text Transformer (FLAN-T5)
- Custom keyword extraction algorithm
- Match score calculation engine
- Contextual text generation

---

## Features

### Core Functionality
- ATS Match Score: Calculates percentage compatibility between resume and job description
- Keyword Analysis: Automatically extracts technical and soft skills from text
- Missing Skills Detection: Identifies gaps in resume compared to job requirements
- AI-Powered Suggestions: Generates personalized improvement recommendations
- Dual Input System: Works with resume alone or with job description for comparison

### User Experience
- Clean, modern dark-themed interface
- Real-time character counting for both inputs
- Animated loading states during analysis
- One-click copy functionality for results
- Fully responsive design for all screen sizes
- Comprehensive error handling with helpful messages

---

## Steps to Run the Project

### Prerequisites
- Python 3.8 or higher installed
- pip package manager
- Minimum 4GB RAM for AI model inference
- Internet connection for initial model download

### Installation

**Step 1: Clone the Repository**
git clone https://github.com/Abhay-Cybersec/ResumeAI.git
cd ResumeAI

text

**Step 2: Create Virtual Environment**

For Windows:
python -m venv venv
venv\Scripts\activate

text

For macOS/Linux:
python3 -m venv venv
source venv/bin/activate

text

**Step 3: Install Dependencies**
pip install -r requirements.txt

text

Note: The first installation will download approximately 3GB of AI model files. This is a one-time download and will be cached locally.

**Step 4: Run the Application**
python app.py

text

Expected output:
==================================================
ResumeAI - Smart Resume Analyzer
INFO:main:Initializing AI model...
INFO:main:Model google/flan-t5-large loaded successfully!
INFO:main:Starting Flask server on http://localhost:5000

text

**Step 5: Access the Application**
1. Open your web browser
2. Navigate to http://localhost:5000
3. Paste your resume text in the first input box
4. Optionally, paste a job description in the second input box
5. Click "Analyze Resume" to receive instant feedback

---

## Project Structure

ResumeAI/
│
├── app.py # Flask backend application
├── templates/
│ └── index.html # Frontend user interface
├── requirements.txt # Python dependencies
├── security_guide.txt # Optional context file
├── README.md # Project documentation
└── .gitignore # Git ignore configuration

text

---

## How It Works

The application follows a multi-step analysis pipeline:

1. User inputs resume text and optionally a job description
2. Flask backend receives the POST request at the /analyze endpoint
3. Keyword extraction algorithm scans both texts for technical skills
4. Match score is calculated based on keyword overlap
5. Missing keywords are identified from job description
6. AI model (FLAN-T5) generates contextual improvement suggestions
7. Results are formatted and returned as JSON
8. Frontend displays comprehensive analysis report

---

## API Documentation

### POST /analyze
Analyzes resume and returns comprehensive feedback.

Request:
{
"resume": "Your resume text here...",
"job_description": "Job description text (optional)"
}

text

Response:
{
"feedback": "Full analysis report",
"match_score": 65,
"missing_keywords": ["docker", "kubernetes"],
"found_keywords": ["python", "react", "sql"]
}

text

### GET /health
Checks API status and model loading state.

### GET /
Returns API information and available endpoints.

---

## Technical Implementation

### Keyword Extraction
The system maintains a curated list of 20+ common technical and soft skills including Python, Java, JavaScript, React, Docker, Kubernetes, AWS, SQL, Git, Machine Learning, and others. The algorithm performs case-insensitive matching against both resume and job description text.

### Match Score Calculation
Match Score = (Matching Keywords / Total Job Keywords) × 100

text

Color coding:
- Green: 70%+ (Excellent match)
- Yellow: 50-69% (Good match)
- Red: Below 50% (Needs improvement)

### AI Model Configuration
- Model: Google FLAN-T5-Large with 780 million parameters
- Max length: 400 tokens
- Temperature: 0.7 for balanced creativity and accuracy
- Device: CPU inference (no GPU required)

---
## Author

Abhay Aggarwal

GitHub: github.com/Abhay-Cybersec

---
