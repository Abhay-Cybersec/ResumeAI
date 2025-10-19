from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline
import os
import logging
import re

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

resume_analyzer = None

def extract_keywords(text):
    """Extract common tech/business keywords from text"""
    common_skills = [
        'python', 'java', 'javascript', 'react', 'node', 'sql', 'mongodb',
        'aws', 'azure', 'gcp', 'docker', 'kubernetes', 'ci/cd', 'git',
        'machine learning', 'ai', 'data science', 'flask', 'django',
        'leadership', 'communication', 'team', 'agile', 'scrum',
        'project management', 'problem solving', 'analytical'
    ]
    
    text_lower = text.lower()
    found_keywords = [skill for skill in common_skills if skill in text_lower]
    return found_keywords

def calculate_match_score(resume_keywords, job_keywords):
    """Calculate percentage match between resume and job description"""
    if not job_keywords:
        return 0
    
    matching = set(resume_keywords) & set(job_keywords)
    return int((len(matching) / len(job_keywords)) * 100)

def initialize_model():
    global resume_analyzer
    try:
        logger.info("Loading HuggingFace model... This may take a few minutes on first run.")
        
        model_name = "google/flan-t5-large"
        
        resume_analyzer = pipeline(
            "text2text-generation",
            model=model_name,
            max_length=512,
            device=-1
        )
        
        logger.info(f"Model {model_name} loaded successfully!")
        return True
    except Exception as e:
        logger.error(f"Error loading model: {str(e)}")
        logger.info("Falling back to a smaller model...")
        try:
            resume_analyzer = pipeline(
                "text2text-generation",
                model="google/flan-t5-base",
                max_length=256,
                device=-1
            )
            logger.info("Fallback model loaded successfully!")
            return True
        except Exception as fallback_error:
            logger.error(f"Fallback model loading failed: {str(fallback_error)}")
            return False

@app.route('/analyze', methods=['POST'])
def analyze_resume():
    try:
        if not request.is_json:
            return jsonify({
                "feedback": "Error: Request must be JSON format"
            }), 400
        
        data = request.json
        resume_text = data.get('resume', '').strip()
        job_description = data.get('job_description', '').strip()
        
        if not resume_text:
            return jsonify({
                "feedback": "Error: No resume text provided"
            }), 400
        
        if len(resume_text) > 15000:
            return jsonify({
                "feedback": "Error: Resume exceeds maximum length"
            }), 400
        
        if resume_analyzer is None:
            logger.info("Model not initialized. Initializing now...")
            if not initialize_model():
                return jsonify({
                    "feedback": "Error: AI model failed to load."
                }), 503
        
        logger.info(f"Analyzing resume ({len(resume_text)} characters)...")
        
        # Extract keywords
        resume_keywords = extract_keywords(resume_text)
        job_keywords = extract_keywords(job_description) if job_description else []
        
        # Calculate match score
        match_score = calculate_match_score(resume_keywords, job_keywords)
        missing_keywords = list(set(job_keywords) - set(resume_keywords))
        
        # Generate AI feedback
        if job_description:
            prompt = f"""Analyze this resume against the job description and provide specific improvement suggestions:

Resume:
{resume_text[:2000]}

Job Description:
{job_description[:1000]}

Provide 3-5 specific suggestions to improve this resume for this job:"""
        else:
            prompt = f"""Analyze this resume and provide 3-5 specific improvement suggestions:

Resume:
{resume_text[:2000]}

Suggestions:"""
        
        result = resume_analyzer(
            prompt,
            max_length=400,
            num_return_sequences=1,
            temperature=0.7,
            do_sample=True
        )
        
        ai_suggestions = result[0]['generated_text'].strip()
        
        # Build comprehensive feedback
        feedback = f"""📊 RESUME ANALYSIS REPORT
{'='*50}

"""
        
        if job_description:
            feedback += f"""🎯 MATCH SCORE: {match_score}%
{'🟢 Excellent Match!' if match_score >= 70 else '🟡 Good Match' if match_score >= 50 else '🔴 Needs Improvement'}

"""
            
            if resume_keywords:
                feedback += f"""✅ FOUND SKILLS ({len(resume_keywords)}):
{', '.join(resume_keywords[:15])}

"""
            
            if missing_keywords:
                feedback += f"""❌ MISSING KEYWORDS ({len(missing_keywords)}):
{', '.join(missing_keywords[:10])}
Consider adding these if you have relevant experience!

"""
        
        else:
            feedback += f"""📝 GENERAL RESUME REVIEW

✅ SKILLS DETECTED ({len(resume_keywords)}):
{', '.join(resume_keywords) if resume_keywords else 'No technical skills detected'}

"""
        
        feedback += f"""💡 AI-POWERED SUGGESTIONS:
{ai_suggestions}

📋 GENERAL TIPS:
• Use action verbs (Led, Developed, Implemented)
• Quantify achievements with numbers (Increased X by 30%)
• Keep it to 1-2 pages
• Use ATS-friendly formatting (no tables/graphics)
• Include relevant keywords from job description
• Proofread for spelling and grammar

🚀 NEXT STEPS:
1. Address the missing keywords (if applicable)
2. Implement AI suggestions above
3. Have someone review your updated resume
4. Tailor for each job application"""
        
        logger.info("Analysis completed successfully")
        
        return jsonify({
            "feedback": feedback,
            "match_score": match_score if job_description else None,
            "missing_keywords": missing_keywords if job_description else [],
            "found_keywords": resume_keywords
        }), 200
    
    except Exception as e:
        logger.error(f"Error during analysis: {str(e)}")
        return jsonify({
            "feedback": f"Error: An unexpected error occurred. {str(e)}"
        }), 500

@app.route('/health', methods=['GET'])
def health_check():
    model_status = "loaded" if resume_analyzer is not None else "not loaded"
    return jsonify({
        "status": "running",
        "model_status": model_status
    }), 200

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "ResumeAI - Smart Resume Analyzer",
        "version": "1.0.0",
        "endpoints": {
            "/analyze": "POST - Analyze resume and get AI feedback",
            "/health": "GET - Check API health status"
        }
    }), 200

if __name__ == '__main__':
    logger.info("=" * 50)
    logger.info("ResumeAI - Smart Resume Analyzer")
    logger.info("=" * 50)
    
    logger.info("Initializing AI model...")
    initialize_model()
    
    logger.info("Starting Flask server on http://localhost:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)
