"""
Mock Interview Agent - Flask Application
Third-Year Computer Engineering College Project
A web-based intelligent mock interview system with real-time feedback, scoring,
and session analytics.
"""

import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

# Load environment configuration
load_dotenv()

from interview_engine import (
    get_engine_status,
    create_session,
    get_session,
    submit_answer_for_session,
    advance_to_next_question,
    finalize_session_report
)

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "mock-interview-agent-secret-key-2026")


@app.route("/")
def index():
    """Renders the main single-page Mock Interview Agent interface."""
    status = get_engine_status()
    return render_template("index.html", status=status)


@app.route("/api/status", methods=["GET"])
def api_status():
    """Returns the backend engine status (Demo vs AI-powered mode)."""
    return jsonify({
        "success": True,
        "data": get_engine_status()
    })


@app.route("/api/start-session", methods=["POST"])
def api_start_session():
    """Initializes a new 5-question interview session."""
    data = request.get_json(silent=True) or {}
    
    role = data.get("role", "Java Developer")
    custom_role = data.get("custom_role", "")
    interview_type = data.get("interview_type", "Technical")
    difficulty = data.get("difficulty", "Beginner")

    valid_roles = ["Java Developer", "Web Developer", "Software Developer", "Other"]
    valid_types = ["Technical", "HR", "Mixed"]
    valid_diffs = ["Beginner", "Intermediate", "Advanced"]

    if role not in valid_roles:
        role = "Software Developer"
    if interview_type not in valid_types:
        interview_type = "Technical"
    if difficulty not in valid_diffs:
        difficulty = "Beginner"

    try:
        session = create_session(role, custom_role, interview_type, difficulty)
        first_q = session["questions"][0]
        
        return jsonify({
            "success": True,
            "data": {
                "session_id": session["id"],
                "role": session["role"],
                "selected_role": session["selected_role"],
                "custom_role": session["custom_role"],
                "interview_type": session["interview_type"],
                "difficulty": session["difficulty"],
                "total_questions": len(session["questions"]),
                "current_index": 0,
                "question_number": 1,
                "question": first_q["question"],
                "category": first_q.get("category", "General"),
                "question_type": first_q.get("type", "Technical")
            }
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": f"Failed to initialize interview session: {str(e)}"
        }), 500


@app.route("/api/submit-answer", methods=["POST"])
def api_submit_answer():
    """Evaluates the submitted answer and returns instant feedback."""
    data = request.get_json(silent=True) or {}
    session_id = data.get("session_id")
    answer = data.get("answer", "")

    if not session_id:
        return jsonify({"success": False, "error": "Missing session_id"}), 400

    try:
        result = submit_answer_for_session(session_id, answer)
        return jsonify({
            "success": True,
            "data": result
        })
    except ValueError as ve:
        return jsonify({"success": False, "error": str(ve)}), 400
    except Exception as e:
        return jsonify({"success": False, "error": f"Evaluation error: {str(e)}"}), 500


@app.route("/api/next-question", methods=["POST"])
def api_next_question():
    """Moves to the next question or returns final report if finished."""
    data = request.get_json(silent=True) or {}
    session_id = data.get("session_id")

    if not session_id:
        return jsonify({"success": False, "error": "Missing session_id"}), 400

    try:
        advancement = advance_to_next_question(session_id)
        return jsonify({
            "success": True,
            "data": advancement
        })
    except ValueError as ve:
        return jsonify({"success": False, "error": str(ve)}), 400
    except Exception as e:
        return jsonify({"success": False, "error": f"Error progressing session: {str(e)}"}), 500


@app.route("/api/end-session", methods=["POST"])
def api_end_session():
    """Prematurely terminates session and returns the consolidated final report."""
    data = request.get_json(silent=True) or {}
    session_id = data.get("session_id")

    if not session_id:
        return jsonify({"success": False, "error": "Missing session_id"}), 400

    try:
        report = finalize_session_report(session_id, status="ended_early")
        return jsonify({
            "success": True,
            "data": {
                "report": report
            }
        })
    except ValueError as ve:
        return jsonify({"success": False, "error": str(ve)}), 400
    except Exception as e:
        return jsonify({"success": False, "error": f"Error ending session: {str(e)}"}), 500


@app.route("/api/session-report/<session_id>", methods=["GET"])
def api_session_report(session_id):
    """Fetches the session report."""
    session = get_session(session_id)
    if not session:
        return jsonify({"success": False, "error": "Session not found"}), 404
        
    report = session.get("report")
    if not report:
        report = finalize_session_report(session_id, status=session.get("status", "in_progress"))

    return jsonify({
        "success": True,
        "data": report
    })


@app.errorhandler(404)
def not_found(e):
    return jsonify({"success": False, "error": "Endpoint not found"}), 404


@app.errorhandler(500)
def server_error(e):
    return jsonify({"success": False, "error": "Internal server error"}), 500


if __name__ == "__main__":
    import sys
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    port = int(os.getenv("FLASK_PORT", 5000))
    debug = os.getenv("FLASK_DEBUG", "False").lower() in ("true", "1", "yes")
    print("\n" + "=" * 65)
    print("[MOCK INTERVIEW AGENT] Computer Engineering College Project")
    print(f"Server running at: http://127.0.0.1:{port}")
    status = get_engine_status()
    print(f"Current Mode: {status['mode_label']}")
    if not status["has_api_key"]:
        print("Notice: Demo Mode active. Set GEMINI_API_KEY in .env to enable real AI.")
    print("=" * 65 + "\n")
    app.run(host="0.0.0.0", port=port, debug=debug)
