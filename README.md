Problem Statement
Job seekers face significant challenges in today's competitive market. Over 70% of resumes are rejected by Applicant Tracking Systems (ATS) before reaching human recruiters. Candidates lack visibility into why their resumes are rejected and struggle to identify missing keywords that match job requirements. There are no accessible tools that provide instant, actionable resume feedback.

ResumeAI addresses this problem by providing AI-powered analysis that helps candidates optimize their resumes, identify skill gaps, and improve their chances of landing interviews.

Tech Stack
Backend
Python 3.12

Flask 3.0.3 - Web framework for REST API

HuggingFace Transformers 4.45.2 - AI model integration

PyTorch 2.4.1 - Deep learning framework

Google FLAN-T5-Large - 780M parameter language model

Flask-CORS 5.0.0 - Cross-origin resource sharing

Frontend
HTML5, CSS3, JavaScript (ES6+)

Tailwind CSS 3.4 - Utility-first styling framework

Feather Icons - Icon library

Responsive design for mobile and desktop

NLP and AI
Text-to-Text Transformer (FLAN-T5)

Custom keyword extraction algorithm

Match score calculation engine

Contextual text generation

Features
Core Functionality
ATS Match Score: Calculates percentage compatibility between resume and job description

Keyword Analysis: Automatically extracts technical and soft skills from text

Missing Skills Detection: Identifies gaps in resume compared to job requirements

AI-Powered Suggestions: Generates personalized improvement recommendations

Dual Input System: Works with resume alone or with job description for comparison

User Experience
Clean, modern dark-themed interface

Real-time character counting for both inputs

Animated loading states during analysis

One-click copy functionality for results

Fully responsive design for all screen sizes

Comprehensive error handling with helpful messages

Project Structure
text
ResumeAI/
│
├── app.py                      # Flask backend application
├── templates/
│   └── index.html             # Frontend user interface
├── requirements.txt           # Python dependencies
├── security_guide.txt         # Optional context file
├── README.md                  # Project documentation
└── .gitignore                 # Git ignore configuration
Installation and Setup
Prerequisites
Python 3.8 or higher installed

pip package manager

Minimum 4GB RAM for AI model inference

Internet connection for initial model download

Step 1: Clone the Repository
bash
git clone https://github.com/yourusername/ResumeAI.git
cd ResumeAI
Step 2: Create Virtual Environment
For Windows:

bash
python -m venv venv
venv\Scripts\activate
For macOS/Linux:

bash
python3 -m venv venv
source venv/bin/activate
Step 3: Install Dependencies
bash
pip install -r requirements.txt
Note: The first installation will download approximately 3GB of AI model files. This is a one-time download and will be cached locally.

Step 4: Run the Application
bash
python app.py
Expected output:

text
==================================================
ResumeAI - Smart Resume Analyzer
==================================================
INFO:__main__:Initializing AI model...
INFO:__main__:Model google/flan-t5-large loaded successfully!
INFO:__main__:Starting Flask server on http://localhost:5000
Step 5: Access the Application
Open your web browser

Navigate to http://localhost:5000

Paste your resume text in the first input box

Optionally, paste a job description in the second input box

Click "Analyze Resume" to receive instant feedback

How It Works
The application follows a multi-step analysis pipeline:

User inputs resume text and optionally a job description

Flask backend receives the POST request at the /analyze endpoint

Keyword extraction algorithm scans both texts for technical skills

Match score is calculated based on keyword overlap

Missing keywords are identified from job description

AI model (FLAN-T5) generates contextual improvement suggestions

Results are formatted and returned as JSON

Frontend displays comprehensive analysis report with match score, skills found, missing keywords, and AI recommendations

API Documentation
POST /analyze
Analyzes resume and returns comprehensive feedback.

Request body:

json
{
  "resume": "Your resume text here...",
  "job_description": "Job description text here (optional)"
}
Response:

json
{
  "feedback": "Full analysis report as formatted text",
  "match_score": 65,
  "missing_keywords": ["docker", "kubernetes", "aws"],
  "found_keywords": ["python", "react", "sql", "git"]
}
GET /health
Checks API status and model loading state.

Response:

json
{
  "status": "running",
  "model_status": "loaded"
}
GET /
Returns API information and available endpoints.

Usage Example
Input Resume:

text
Software Engineer with 2 years experience
Skills: Python, React, SQL, Git
Built web applications and REST APIs
Input Job Description:

text
Senior Developer position
Requirements: Python, React, Docker, Kubernetes, AWS
3+ years experience required
Output Analysis:

text
RESUME ANALYSIS REPORT
==================================================

MATCH SCORE: 55%
Status: Good Match

FOUND SKILLS (4): python, react, sql, git

MISSING KEYWORDS (3): docker, kubernetes, aws
Consider adding these if you have relevant experience.

AI-POWERED SUGGESTIONS:
1. Add Docker and Kubernetes experience if you have it
2. Include AWS or cloud platform projects
3. Quantify achievements with specific metrics
4. Add leadership or team collaboration examples
5. Extend experience section with measurable results

GENERAL TIPS:
- Use action verbs (Led, Developed, Implemented)
- Quantify achievements with numbers
- Keep resume to 1-2 pages
- Use ATS-friendly formatting
- Include relevant keywords from job description
- Proofread for spelling and grammar errors
Technical Implementation Details
Keyword Extraction
The system maintains a curated list of 20+ common technical and soft skills including Python, Java, JavaScript, React, Docker, Kubernetes, AWS, SQL, Git, Machine Learning, and others. The algorithm performs case-insensitive matching against both resume and job description text.

Match Score Calculation
text
Match Score = (Number of Matching Keywords / Total Job Keywords) × 100
Color coding:

Green (70%+): Excellent match

Yellow (50-69%): Good match

Red (<50%): Needs improvement

AI Model
Uses Google FLAN-T5-Large with 780 million parameters. The model is configured with:

Max length: 400 tokens

Temperature: 0.7 for balanced creativity and accuracy

Device: CPU inference (no GPU required)
