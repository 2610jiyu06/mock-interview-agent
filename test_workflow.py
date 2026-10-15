"""
Automated Test Suite for Mock Interview Agent
Tests complete end-to-end user workflow:
1. Engine Status Verification
2. Session Initialization across different roles and types
3. Question Progression (5 questions)
4. Answer Submission & Heuristic Scoring (Empty, Short, Detailed)
5. Session Finalization & Report Generation (Total Score, Average Score, History)
6. Early Session Termination (End Interview)
"""

import sys
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

from app import app

def run_tests():
    print("=" * 60)
    print("[TEST SUITE] Running Tests for Mock Interview Agent...")
    print("=" * 60)

    client = app.test_client()

    # Test 1: Home page loads successfully
    print("\n[Test 1] Testing GET / (Home Page)...")
    res = client.get("/")
    assert res.status_code == 200, f"Expected 200, got {res.status_code}"
    html = res.data.decode("utf-8")
    assert "Mock Interview Agent" in html, "Brand title not found in HTML"
    assert "Java Developer" in html, "Target roles not found in HTML"
    assert "status-badge" in html, "Status badge not found in HTML"
    print("   [PASS] Test 1: Home page rendered with HTML5 layout.")

    # Test 2: Engine status endpoint
    print("\n[Test 2] Testing GET /api/status...")
    res = client.get("/api/status")
    assert res.status_code == 200, f"Expected 200, got {res.status_code}"
    status_json = res.get_json()
    assert status_json["success"] is True, "Status call failed"
    status_data = status_json["data"]
    print(f"   Detected Mode: {status_data['mode_label']}")
    print(f"   Has API Key: {status_data['has_api_key']}")
    print(f"   Model: {status_data['model']}")
    assert status_data["mode"] in ["demo", "ai"], "Invalid mode"
    print("   [PASS] Test 2: API status returns correct metadata.")

    # Test 3: Session Creation (Java Developer, Technical, Beginner)
    print("\n[Test 3] Testing POST /api/start-session (Java Developer, Technical, Beginner)...")
    payload = {
        "role": "Java Developer",
        "custom_role": "",
        "interview_type": "Technical",
        "difficulty": "Beginner"
    }
    res = client.post("/api/start-session", json=payload)
    assert res.status_code == 200, f"Expected 200, got {res.status_code}"
    session_res = res.get_json()
    assert session_res["success"] is True
    session_data = session_res["data"]
    session_id = session_data["session_id"]
    assert session_data["total_questions"] == 5, f"Expected 5 questions, got {session_data['total_questions']}"
    assert session_data["question_number"] == 1
    assert len(session_data["question"]) > 10
    print(f"   Created Session ID: {session_id}")
    print(f"   Question 1: {session_data['question'][:70]}...")
    print("   [PASS] Test 3: Session created with 5 curated questions.")

    # Test 4: Answer Evaluation - Question 1 with a detailed answer
    print("\n[Test 4] Testing Answer Submission (Question 1 with detailed response)...")
    detailed_answer = (
        "JDK (Java Development Kit) contains the compiler (javac), debugger, and full toolset required for development. "
        "JRE (Java Runtime Environment) provides the standard libraries and runtime environment to execute programs. "
        "JVM (Java Virtual Machine) executes bytecode (.class files) line-by-line or via JIT compilation into native machine code. "
        "Java is platform-independent because source code compiles into bytecode, and any platform-specific JVM can execute it."
    )
    res = client.post("/api/submit-answer", json={"session_id": session_id, "answer": detailed_answer})
    assert res.status_code == 200, f"Expected 200, got {res.status_code}"
    eval_res = res.get_json()
    assert eval_res["success"] is True
    eval_data = eval_res["data"]
    evaluation = eval_data["evaluation"]
    print(f"   Score: {evaluation['score_display']}")
    print(f"   Reason: {evaluation['reason']}")
    print(f"   Strengths count: {len(evaluation['strengths'])}")
    print(f"   Improvements count: {len(evaluation['areas_to_improve'])}")
    print(f"   Evaluation Mode: {evaluation['mode_used']}")
    assert evaluation["score"] >= 7.0, f"Expected score >= 7.0 for thorough answer, got {evaluation['score']}"
    assert len(evaluation["strengths"]) > 0, "No strengths generated"
    assert len(evaluation["areas_to_improve"]) > 0, "No improvements generated"
    assert len(evaluation["sample_answer"]) > 20, "No sample answer generated"
    print("   [PASS] Test 4: Detailed answer received high score and constructive feedback.")

    # Test 5: Progression through Questions 2, 3, 4, 5
    sample_answers = [
        "Encapsulation binds data and methods together with private access modifiers and public getters and setters.",
        "The == operator checks memory reference equality while .equals() compares string value content.",
        "ArrayList is backed by dynamic array with O(1) random access while LinkedList is doubly linked.",
        "Checked exceptions are verified at compile-time while unchecked happen at runtime."
    ]

    for q_idx in range(2, 6):
        print(f"\n[Test 5.{q_idx}] Progressing to Question {q_idx}...")
        res = client.post("/api/next-question", json={"session_id": session_id})
        assert res.status_code == 200, f"Expected 200, got {res.status_code}"
        next_data = res.get_json()["data"]
        assert next_data["has_next"] is True
        assert next_data["question_number"] == q_idx
        print(f"   Question {q_idx}: {next_data['question'][:65]}...")

        # Submit answer
        ans_text = sample_answers[q_idx - 2]
        res_sub = client.post("/api/submit-answer", json={"session_id": session_id, "answer": ans_text})
        assert res_sub.status_code == 200
        sub_data = res_sub.get_json()["data"]
        print(f"   Evaluated Q{q_idx}: Score {sub_data['evaluation']['score_display']}")
        if q_idx == 5:
            assert sub_data["is_last_question"] is True, "5th question should be marked as is_last_question"

    print("   [PASS] Test 5: Successfully progressed through all 5 questions.")

    # Test 6: Finalizing Session to get Final Report
    print("\n[Test 6] Finalizing Session and Generating Report...")
    res = client.post("/api/next-question", json={"session_id": session_id})
    assert res.status_code == 200
    final_data = res.get_json()["data"]
    assert final_data["has_next"] is False, "Should have no more questions"
    report = final_data["report"]
    print(f"   Total Score: {report['total_score']} / {report['max_possible_score']}")
    print(f"   Average Score: {report['average_score']} / 10")
    print(f"   Verdict: {report['performance_verdict']}")
    print(f"   Consolidated Strengths: {len(report['consolidated_strengths'])}")
    print(f"   Consolidated Improvements: {len(report['consolidated_improvements'])}")
    print(f"   History Items: {len(report['history'])}")
    assert report["questions_answered"] == 5
    assert len(report["history"]) == 5
    assert len(report["consolidated_strengths"]) > 0
    assert len(report["consolidated_improvements"]) > 0
    print("   [PASS] Test 6: Final Report generated with full metrics and 5-item history.")

    # Test 7: Custom Role & Early End Interview
    print("\n[Test 7] Testing Custom Role ('Cloud DevOps Engineer') & Early Termination...")
    res = client.post("/api/start-session", json={
        "role": "Other",
        "custom_role": "Cloud DevOps Engineer",
        "interview_type": "Mixed",
        "difficulty": "Intermediate"
    })
    assert res.status_code == 200
    sess_devops = res.get_json()["data"]
    devops_id = sess_devops["session_id"]
    assert sess_devops["role"] == "Cloud DevOps Engineer"

    # Submit 1 answer then end early
    client.post("/api/submit-answer", json={
        "session_id": devops_id,
        "answer": "Deadlocks occur when processes hold resources and wait for others in a circular dependency."
    })

    res_end = client.post("/api/end-session", json={"session_id": devops_id})
    assert res_end.status_code == 200
    early_report = res_end.get_json()["data"]["report"]
    assert early_report["questions_answered"] == 1
    assert early_report["status"] == "ended_early"
    print(f"   Early Ended Session: Answered {early_report['questions_answered']} questions, Status: {early_report['status']}")
    print("   [PASS] Test 7: Custom role and early session termination work seamlessly.")

    # Test 8: Empty and minimal answer edge cases
    print("\n[Test 8] Testing Edge Cases: Empty & Short Answers...")
    res = client.post("/api/start-session", json={"role": "Web Developer", "interview_type": "Technical", "difficulty": "Beginner"})
    edge_id = res.get_json()["data"]["session_id"]
    
    # Empty answer
    res_empty = client.post("/api/submit-answer", json={"session_id": edge_id, "answer": ""})
    assert res_empty.status_code == 200
    assert res_empty.get_json()["data"]["evaluation"]["score"] == 0.0

    # Advance and test short answer
    client.post("/api/next-question", json={"session_id": edge_id})
    res_short = client.post("/api/submit-answer", json={"session_id": edge_id, "answer": "it is fast"})
    assert res_short.status_code == 200
    assert res_short.get_json()["data"]["evaluation"]["score"] <= 3.5
    print("   [PASS] Test 8: Edge cases properly graded without exceptions.")

    print("\n" + "=" * 60)
    print("[SUCCESS] ALL 8 TESTS PASSED COMPLETELY!")
    print("=" * 60)

if __name__ == "__main__":
    run_tests()
