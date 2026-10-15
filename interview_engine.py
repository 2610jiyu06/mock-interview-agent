"""
Mock Interview Agent - Core Interview Engine
Handles session state, dual-mode evaluation (AI Generative via Gemini/OpenAI + Offline Heuristic Rule-Based),
question progression, and final report generation.
"""

import os
import re
import json
import uuid
import time
import requests
from dotenv import load_dotenv
from question_bank import get_questions_for_session, QUESTION_BANK

# Load environment variables from .env file
load_dotenv()

# In-memory storage for active interview sessions
SESSIONS = {}


def get_api_credentials():
    """
    Checks for available API keys in environment or .env.
    Returns provider info and verification flag.
    """
    gemini_key = os.getenv("GEMINI_API_KEY", "").strip() or os.getenv("GOOGLE_API_KEY", "").strip()
    openai_key = os.getenv("OPENAI_API_KEY", "").strip()
    gemini_model = os.getenv("GEMINI_MODEL", "gemini-1.5-flash").strip()

    if gemini_key:
        return {
            "configured": True,
            "provider": "Google Gemini",
            "model": gemini_model,
            "api_key": gemini_key
        }
    elif openai_key:
        return {
            "configured": True,
            "provider": "OpenAI",
            "model": "gpt-4o-mini",
            "api_key": openai_key
        }
    else:
        return {
            "configured": False,
            "provider": None,
            "model": "Curated Rule-Based Engine",
            "api_key": None
        }


def get_engine_status():
    """Returns application mode status for UI indicators."""
    creds = get_api_credentials()
    if creds["configured"]:
        return {
            "mode": "ai",
            "mode_label": f"AI-Powered ({creds['provider']})",
            "provider": creds["provider"],
            "model": creds["model"],
            "has_api_key": True,
            "badge_color": "green",
            "notice": f"Connected to {creds['provider']} ({creds['model']}). Real-time generative feedback is active."
        }
    else:
        return {
            "mode": "demo",
            "mode_label": "Demo Mode (Offline / Rule-Based)",
            "provider": "Offline Heuristic Evaluator",
            "model": "Curated Computer Engineering Question Bank",
            "has_api_key": False,
            "badge_color": "amber",
            "notice": "No LLM API key detected in .env. Running in Demo Mode with curated interview questions and transparent heuristic evaluation. To enable real AI, add GEMINI_API_KEY to your .env file."
        }


def call_gemini_api(api_key: str, model: str, prompt: str, system_instruction: str = "") -> str:
    """
    Calls the Google Gemini REST API directly using requests.
    Supports v1beta generateContent endpoint with robust error handling.
    """
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
    headers = {"Content-Type": "application/json"}
    
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ],
        "generationConfig": {
            "temperature": 0.4,
            "maxOutputTokens": 1024,
            "responseMimeType": "application/json"
        }
    }

    if system_instruction:
        payload["systemInstruction"] = {
            "parts": [{"text": system_instruction}]
        }

    response = requests.post(url, headers=headers, json=payload, timeout=20)
    response.raise_for_status()
    data = response.json()
    
    candidates = data.get("candidates", [])
    if not candidates:
        raise ValueError("No candidate responses returned from Gemini.")
    
    parts = candidates[0].get("content", {}).get("parts", [])
    if not parts:
        raise ValueError("Empty content returned from Gemini.")
        
    return parts[0].get("text", "")


def call_openai_api(api_key: str, model: str, prompt: str, system_instruction: str = "") -> str:
    """Calls OpenAI chat completions API directly using requests."""
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    messages = []
    if system_instruction:
        messages.append({"role": "system", "content": system_instruction})
    messages.append({"role": "user", "content": prompt})
    
    payload = {
        "model": model or "gpt-4o-mini",
        "messages": messages,
        "temperature": 0.4,
        "response_format": {"type": "json_object"}
    }
    
    response = requests.post(url, headers=headers, json=payload, timeout=20)
    response.raise_for_status()
    data = response.json()
    return data["choices"][0]["message"]["content"]


def call_llm(prompt: str, system_instruction: str = "") -> str:
    """Dispatches prompt to configured LLM (Gemini or OpenAI)."""
    creds = get_api_credentials()
    if not creds["configured"]:
        raise ValueError("No API credentials configured.")
    
    if creds["provider"] == "Google Gemini":
        return call_gemini_api(creds["api_key"], creds["model"], prompt, system_instruction)
    elif creds["provider"] == "OpenAI":
        return call_openai_api(creds["api_key"], creds["model"], prompt, system_instruction)
    else:
        raise ValueError(f"Unknown provider: {creds['provider']}")


def evaluate_answer_rule_based(question_obj: dict, answer: str, role: str, difficulty: str) -> dict:
    """
    Transparent, intelligent heuristic rule-based evaluator for Demo Mode.
    Evaluates answer depth, keyword coverage, structured reasoning, and communication clarity.
    Returns score out of 10, reason, strengths, areas to improve, and sample answer.
    """
    trimmed = answer.strip()
    words = re.findall(r'\b[A-Za-z0-9_-]+\b', trimmed)
    word_count = len(words)
    lower_answer = trimmed.lower()

    keywords = question_obj.get("keywords", [])
    ideal_concepts = question_obj.get("ideal_concepts", [])
    sample_answer = question_obj.get("sample_answer", "")
    is_hr = question_obj.get("type", "Technical") == "HR"

    # Edge Case 1: Empty or almost empty answer
    if word_count == 0:
        return {
            "score": 0.0,
            "score_display": "0.0 / 10",
            "reason": "No response was submitted. In an interview, leaving a question blank conveys an inability to address the topic.",
            "strengths": [
                "The question was received, but no content was provided to evaluate."
            ],
            "areas_to_improve": [
                "Attempt to outline basic definitions or related concepts even if you are unsure of the complete answer.",
                "Mention related technologies or how you would approach researching the solution."
            ],
            "sample_answer": sample_answer,
            "mode_used": "Demo Mode (Rule-Based Heuristic)"
        }

    # Edge Case 2: Minimalist / single-word answer
    if word_count < 10:
        return {
            "score": 2.5,
            "score_display": "2.5 / 10",
            "reason": "The answer is extremely brief (under 10 words). Technical and HR interviewers require substantive explanations with definitions, mechanics, and examples.",
            "strengths": [
                "Recognized the general prompt topic."
            ],
            "areas_to_improve": [
                "Provide complete sentences explaining the underlying mechanisms rather than a one-line summary.",
                "Include concrete examples or use cases to demonstrate real-world comprehension.",
                "Structure your thoughts using a clear opening statement followed by supporting details."
            ],
            "sample_answer": sample_answer,
            "mode_used": "Demo Mode (Rule-Based Heuristic)"
        }

    # Keyword and Concept Matching
    matched_keywords = []
    missing_keywords = []
    for kw in keywords:
        # Check if keyword or phrase appears in candidate's answer
        if kw.lower() in lower_answer:
            matched_keywords.append(kw)
        else:
            missing_keywords.append(kw)

    keyword_ratio = len(matched_keywords) / max(len(keywords), 1)

    # Structural Signals
    has_example_words = any(w in lower_answer for w in ["for example", "such as", "for instance", "in my project", "scenario", "use case", "experience"])
    has_contrast_words = any(w in lower_answer for w in ["whereas", "in contrast", "while", "difference", "however", "on the other hand", "alternatively"])
    has_star_signals = any(w in lower_answer for w in ["situation", "task", "action", "result", "outcome", "learned", "delivered", "resolved"])

    # Base score calculation based on word count & depth
    if word_count < 25:
        base_score = 4.5
    elif word_count < 60:
        base_score = 6.0
    elif word_count < 150:
        base_score = 7.5
    else:
        base_score = 8.2

    # Bonus / penalty adjustments
    bonus = 0.0
    # Keyword bonus up to +1.8
    bonus += (keyword_ratio * 1.8)

    if has_example_words:
        bonus += 0.5
    if has_contrast_words:
        bonus += 0.4
    if is_hr and has_star_signals:
        bonus += 0.6

    # Difficulty calibration
    if difficulty == "Advanced" and word_count < 40:
        bonus -= 0.8
    elif difficulty == "Beginner" and keyword_ratio > 0.4:
        bonus += 0.4

    raw_score = base_score + bonus
    # Clamp between 2.0 and 9.5 (or 9.8 for exceptional depth)
    final_score = max(2.5, min(9.5, round(raw_score, 1)))
    if keyword_ratio >= 0.75 and word_count >= 80 and has_example_words:
        final_score = min(9.8, round(final_score + 0.5, 1))

    # Constructive Strengths
    strengths = []
    if matched_keywords:
        sample_terms = ", ".join([f"'{k}'" for k in matched_keywords[:4]])
        strengths.append(f"Successfully incorporated key domain terminology: {sample_terms}.")
    else:
        strengths.append("Addressed the general context of the question clearly.")

    if word_count >= 50:
        strengths.append(f"Good explanatory length ({word_count} words), allowing adequate room to articulate your reasoning.")
    else:
        strengths.append("Kept the answer concise and straightforward.")

    if has_example_words:
        strengths.append("Effectively utilized examples or use cases to illustrate conceptual points.")
    elif is_hr and has_star_signals:
        strengths.append("Adopted structured storytelling reflecting elements of the STAR method (Situation, Task, Action, Result).")
    elif has_contrast_words:
        strengths.append("Highlighted differences and comparative trade-offs between options.")

    # Constructive Areas to Improve
    areas_to_improve = []
    if missing_keywords and len(missing_keywords) >= 2:
        missing_terms = ", ".join([f"'{k}'" for k in missing_keywords[:3]])
        areas_to_improve.append(f"Deepen the technical explanation by discussing crucial concepts such as {missing_terms}.")
    
    if not has_example_words:
        areas_to_improve.append("Ground theoretical explanations in tangible scenarios (e.g., 'In an e-commerce checkout service...' or 'In a high-throughput API...').")

    if word_count < 45:
        areas_to_improve.append("Elaborate on the 'why' and 'how' behind your answer rather than just stating high-level definitions.")

    if is_hr and not has_star_signals:
        areas_to_improve.append("For behavioral questions, follow the STAR framework: clearly describe the Situation, your specific Task, the Action you executed, and the measurable Result.")

    if not areas_to_improve:
        areas_to_improve.append("Consider touching upon performance trade-offs, edge cases, or scalability considerations to achieve a perfect 10.")

    # Detailed Reason Synthesis
    if final_score >= 8.5:
        reason = f"Excellent response! You demonstrated deep comprehension of the topic with strong technical terminology and clear structure ({word_count} words)."
    elif final_score >= 7.0:
        reason = f"Good solid answer. You covered the primary concepts and key principles well, but expanding further on practical edge cases or implementation details would make it outstanding."
    elif final_score >= 5.5:
        reason = f"Fair foundational answer. You captured the surface definition, but an interviewer would expect more technical depth and specific terminology regarding underlying mechanics."
    else:
        reason = f"Needs improvement. The response was either too brief ({word_count} words) or missed fundamental concepts expected for a {role} at the {difficulty} level."

    return {
        "score": final_score,
        "score_display": f"{final_score:.1f} / 10",
        "reason": reason,
        "strengths": strengths[:3],
        "areas_to_improve": areas_to_improve[:3],
        "sample_answer": sample_answer,
        "mode_used": "Demo Mode (Rule-Based Heuristic)"
    }


def evaluate_answer_ai(question_obj: dict, answer: str, role: str, difficulty: str) -> dict:
    """
    Evaluates answer using configured real LLM (Gemini or OpenAI).
    Falls back gracefully to rule-based evaluation if API call fails.
    """
    system_instruction = (
        "You are an expert technical interviewer and hiring manager at a top technology company. "
        "Your goal is to evaluate student and candidate responses constructively for a college mock interview. "
        "Always be encouraging yet rigorously honest. Return your evaluation strictly in valid JSON format."
    )

    prompt = f"""
Evaluate the candidate's answer for the following mock interview question.

Role: {role}
Difficulty Level: {difficulty}
Question Category: {question_obj.get('category', 'Technical')}
Interview Question: {question_obj.get('question')}
Target Concepts / Keywords: {', '.join(question_obj.get('keywords', []))}

Candidate's Submitted Answer:
\"\"\"
{answer}
\"\"\"

Produce a JSON response with exactly this schema:
{{
  "score": <float number between 0.0 and 10.0, rounded to 1 decimal place>,
  "reason": "<A 2-3 sentence clear, professional explanation of why this score was awarded>",
  "strengths": [
    "<1-2 sentences on a specific strong point in the candidate's response>",
    "<1-2 sentences on another specific strength>"
  ],
  "areas_to_improve": [
    "<1-2 sentences giving an actionable recommendation for what was missing or could be improved>",
    "<1-2 sentences giving another actionable improvement recommendation>"
  ],
  "sample_answer": "<A comprehensive, exemplary answer illustrating how a top-tier candidate should answer this question, formatted with clean paragraphs>"
}}
"""

    try:
        raw_text = call_llm(prompt, system_instruction)
        
        # Clean potential markdown fences ```json ... ```
        cleaned_json = raw_text.strip()
        if cleaned_json.startswith("```"):
            cleaned_json = re.sub(r"^```(?:json)?\s*", "", cleaned_json)
            cleaned_json = re.sub(r"\s*```$", "", cleaned_json)
        
        parsed = json.loads(cleaned_json)
        score = float(parsed.get("score", 7.0))
        score = max(0.0, min(10.0, round(score, 1)))

        return {
            "score": score,
            "score_display": f"{score:.1f} / 10",
            "reason": parsed.get("reason", "Good effort demonstrating relevant knowledge."),
            "strengths": parsed.get("strengths", ["Addressed the core question."]),
            "areas_to_improve": parsed.get("areas_to_improve", ["Add more depth and real-world examples."]),
            "sample_answer": parsed.get("sample_answer", question_obj.get("sample_answer", "")),
            "mode_used": f"AI-Evaluated ({get_api_credentials()['provider']})"
        }
    except Exception as e:
        # Fall back to rule-based evaluation gracefully so the student's interview never breaks
        fallback = evaluate_answer_rule_based(question_obj, answer, role, difficulty)
        fallback["mode_used"] = f"Demo Mode (Fell back from AI: {str(e)[:45]}...)"
        return fallback


def create_session(role: str, custom_role: str, interview_type: str, difficulty: str) -> dict:
    """
    Initializes a new interview session.
    Fetches 5 questions curated for the selection.
    """
    effective_role = custom_role.strip() if role == "Other" and custom_role.strip() else role
    session_id = str(uuid.uuid4())
    
    # 5 questions per session as required
    questions = get_questions_for_session(role, interview_type, difficulty, count=5)
    
    session = {
        "id": session_id,
        "role": effective_role,
        "selected_role": role,
        "custom_role": custom_role,
        "interview_type": interview_type,
        "difficulty": difficulty,
        "questions": questions,
        "current_index": 0,
        "answers": [],
        "evaluations": [],
        "created_at": time.time(),
        "status": "in_progress", # in_progress, completed, ended_early
        "report": None
    }
    
    SESSIONS[session_id] = session
    return session


def get_session(session_id: str) -> dict:
    """Retrieves session from in-memory store."""
    return SESSIONS.get(session_id)


def submit_answer_for_session(session_id: str, answer_text: str) -> dict:
    """
    Processes the candidate's answer for the current question in the session.
    Generates evaluation, saves to history, and checks if session is complete.
    """
    session = SESSIONS.get(session_id)
    if not session:
        raise ValueError("Interview session not found.")
        
    idx = session["current_index"]
    if idx >= len(session["questions"]):
        raise ValueError("All questions for this session have already been answered.")
        
    current_q = session["questions"][idx]
    
    # Check credentials to choose evaluation engine
    creds = get_api_credentials()
    if creds["configured"]:
        eval_result = evaluate_answer_ai(current_q, answer_text, session["role"], session["difficulty"])
    else:
        eval_result = evaluate_answer_rule_based(current_q, answer_text, session["role"], session["difficulty"])
        
    session["answers"].append(answer_text)
    session["evaluations"].append(eval_result)
    
    is_last = (idx == len(session["questions"]) - 1)
    
    return {
        "session_id": session_id,
        "question_index": idx,
        "question_number": idx + 1,
        "total_questions": len(session["questions"]),
        "question": current_q["question"],
        "category": current_q.get("category", "General"),
        "candidate_answer": answer_text,
        "evaluation": eval_result,
        "is_last_question": is_last
    }


def advance_to_next_question(session_id: str) -> dict:
    """Advances current_index to the next question."""
    session = SESSIONS.get(session_id)
    if not session:
        raise ValueError("Interview session not found.")
        
    session["current_index"] += 1
    idx = session["current_index"]
    
    if idx < len(session["questions"]):
        next_q = session["questions"][idx]
        return {
            "session_id": session_id,
            "has_next": True,
            "question_index": idx,
            "question_number": idx + 1,
            "total_questions": len(session["questions"]),
            "question": next_q["question"],
            "category": next_q.get("category", "Technical"),
            "type": next_q.get("type", session["interview_type"]),
            "difficulty": session["difficulty"],
            "role": session["role"]
        }
    else:
        # No more questions; generate final report
        report = finalize_session_report(session_id, status="completed")
        return {
            "session_id": session_id,
            "has_next": False,
            "report": report
        }


def finalize_session_report(session_id: str, status: str = "completed") -> dict:
    """
    Computes total score, average score, consolidated strengths, areas to improve,
    and formats the complete interview history for the session.
    """
    session = SESSIONS.get(session_id)
    if not session:
        raise ValueError("Interview session not found.")
        
    session["status"] = status
    evals = session.get("evaluations", [])
    questions = session.get("questions", [])
    answers = session.get("answers", [])
    
    num_answered = len(evals)
    
    if num_answered == 0:
        total_score = 0.0
        avg_score = 0.0
        performance_verdict = "Session ended before any answers were submitted."
    else:
        total_score = round(sum(e["score"] for e in evals), 1)
        avg_score = round(total_score / num_answered, 1)
        
        if avg_score >= 8.5:
            performance_verdict = "Outstanding Performance! High technical command, clear structure, and ready for industry interviews."
        elif avg_score >= 7.0:
            performance_verdict = "Strong Performance! Good technical foundation with minor opportunities to deepen practical examples."
        elif avg_score >= 5.0:
            performance_verdict = "Developing Foundation. Good effort; review recommended keywords and practice structured answers."
        else:
            performance_verdict = "Needs Significant Improvement. Focus on fundamental concepts and practice answering in complete detail."

    # Consolidate top strengths and areas for improvement
    all_strengths = []
    all_improvements = []
    for e in evals:
        all_strengths.extend(e.get("strengths", []))
        all_improvements.extend(e.get("areas_to_improve", []))

    # De-duplicate while preserving order
    def dedupe(seq):
        seen = set()
        res = []
        for x in seq:
            if x not in seen:
                seen.add(x)
                res.append(x)
        return res

    consolidated_strengths = dedupe(all_strengths)[:5]
    consolidated_improvements = dedupe(all_improvements)[:5]

    # Build detailed history items
    history = []
    for i in range(num_answered):
        q = questions[i]
        ans = answers[i]
        e = evals[i]
        history.append({
            "question_number": i + 1,
            "question": q["question"],
            "category": q.get("category", "General"),
            "type": q.get("type", "Technical"),
            "answer": ans,
            "score": e["score"],
            "score_display": e["score_display"],
            "reason": e["reason"],
            "strengths": e["strengths"],
            "areas_to_improve": e["areas_to_improve"],
            "sample_answer": e["sample_answer"],
            "mode_used": e.get("mode_used", "Standard")
        })

    report = {
        "session_id": session_id,
        "role": session["role"],
        "interview_type": session["interview_type"],
        "difficulty": session["difficulty"],
        "total_questions": len(questions),
        "questions_answered": num_answered,
        "total_score": total_score,
        "max_possible_score": num_answered * 10,
        "average_score": avg_score,
        "performance_verdict": performance_verdict,
        "consolidated_strengths": consolidated_strengths,
        "consolidated_improvements": consolidated_improvements,
        "history": history,
        "status": status
    }
    
    session["report"] = report
    return report
