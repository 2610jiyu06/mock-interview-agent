# 🎓 Mock Interview Agent

> **Third-Year Computer Engineering College Project**  
> An intelligent, full-stack mock interview platform designed to help computer engineering students prepare for campus placements and technical interviews through structured, real-time evaluation and actionable feedback.

---

## 📌 Project Overview

**Mock Interview Agent** is an interactive web application built with a **Python Flask** backend and a responsive **HTML5/CSS3/JavaScript** frontend. It simulates real-world engineering job interviews by presenting one targeted question at a time across diverse technical and behavioral domains.

### 🌟 Key Highlights

- **Tailored Role Selection**: Choose from **Java Developer**, **Web Developer**, **Software Developer**, or specify a custom role under **Other** (e.g., *DevOps Engineer*, *Data Engineer*).
- **Flexible Interview Formats**: Practice **Technical**, **HR / Behavioral (STAR method)**, or **Mixed** interviews (3 Technical + 2 HR).
- **Multiple Difficulty Tiers**: **Beginner**, **Intermediate**, and **Advanced** challenge levels.
- **Instant Structured Evaluation**: Every submitted response receives:
  - 📊 **Score out of 10** with visual color-coded badge.
  - 📝 **Detailed Scoring Rationale**.
  - ✅ **Demonstrated Key Strengths**.
  - 💡 **Actionable Areas for Improvement**.
  - 🏆 **Exemplary Model Answer** illustrating how top-tier candidates address the topic.
- **5 Questions Per Session**: Complete, focused interview loops with live session timer and progress tracking.
- **Comprehensive Final Scorecard**:
  - Total Points (out of 50) and Average Score (out of 10).
  - Overall Performance Verdict.
  - Consolidated list of top strengths and growth areas.
  - Complete **Interview History** with side-by-side comparison of candidate responses vs. model answers.
  - 🖨️ **One-Click Print / PDF Export** (`@media print` stylesheet) for academic submissions and portfolio reviews.
- **Dual-Mode Evaluation Architecture**:
  - 🟡 **Demo Mode (Default)**: Fully offline and functional out-of-the-box using curated Computer Engineering question banks and an intelligent heuristic scoring engine. No API key required!
  - 🟢 **AI-Powered Mode**: Seamlessly connects to real generative LLMs (**Google Gemini** or **OpenAI**) via server-side API calls. API keys are strictly kept server-side and never exposed to the frontend.

---

## 🎨 UI/UX Design

- **Color Palette**: Clean white background (`#ffffff` / `#f8fafc`) with authoritative navy-blue accents (`#0b2545`, `#134074`, `#1d4ed8`).
- **Typography**: Crisp, highly readable typography powered by `Inter` and `JetBrains Mono`.
- **Card-Based Hierarchy**: Clear visual boundaries, gentle shadows, and intuitive status badges.
- **Responsive Layout**: Designed for desktops, laptops, tablets, and smartphones.

---

## 🏗️ System Architecture

```
                      +---------------------------------------+
                      |          Client Browser (UI)          |
                      |   HTML5 + CSS3 + Vanilla JavaScript   |
                      +---------------------------------------+
                                          |
                                HTTP REST API Calls
                          (JSON Payloads / No API Keys)
                                          |
                                          v
                      +---------------------------------------+
                      |         Flask Backend (app.py)        |
                      |        Session & Route Manager        |
                      +---------------------------------------+
                                          |
                      +---------------------------------------+
                      |   Interview Engine (interview_engine) |
                      +---------------------------------------+
                                     /         \
                         (No API Key)           (API Key Found in .env)
                                   /             \
                                  v               v
                +-------------------+   +-------------------------+
                |     Demo Mode     |   |      AI-Powered Mode    |
                |  Heuristic Engine |   |  Google Gemini / OpenAI |
                |  + Question Bank  |   |    REST API (Server)    |
                +-------------------+   +-------------------------+
```

---

## 📂 Project Directory Structure

```text
Mock Interview Agent/
│
├── app.py                  # Flask web server and REST API endpoints
├── interview_engine.py     # Session manager, AI caller, and rule-based grader
├── question_bank.py        # Curated questions, keywords, and model answers
├── test_workflow.py        # Automated test suite (8 test cases)
│
├── requirements.txt        # Minimal Python dependencies
├── .env.example            # Template for environment configuration
├── .env                    # Local secrets (excluded from Git)
├── .gitignore              # Protects secrets, cache, and virtual environments
├── README.md               # College project documentation and viva guide
│
├── templates/
│   └── index.html          # Semantic HTML5 single-page application template
│
└── static/
    ├── css/
    │   └── style.css       # Navy-blue and white responsive design + print styles
    └── js/
        └── app.js          # Clientside controller, session transitions, timer, DOM
```

---

## 💻 Windows Setup Instructions

Follow these step-by-step instructions to run the project on Windows.

### Prerequisites

- **Python 3.10, 3.11, 3.12, 3.13, or 3.14** installed on your machine.
- Verify your Python installation by running:
  ```powershell
  python --version
  ```

---

### Step 1: Open the Project Directory

Open **PowerShell** or **Command Prompt** (cmd) and navigate to the project directory:

```powershell
cd "c:\Users\DELL\Desktop\Mock Interview Agent"
```

---

### Step 2: (Recommended) Create and Activate a Virtual Environment

Creating an isolated virtual environment ensures clean dependency management:

**Using PowerShell:**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```
*(If you see an execution policy error in PowerShell, run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` and then run the activate command again).*

**Using Command Prompt (cmd.exe):**
```cmd
python -m venv venv
venv\Scripts\activate.bat
```

---

### Step 3: Install Required Dependencies

Install the lightweight requirements:

```powershell
python -m pip install -r requirements.txt
```

*Dependencies installed:*
- `Flask` (>= 3.0.0): Lightweight, standard Python web framework.
- `python-dotenv` (>= 1.0.0): Loads secrets safely from `.env`.
- `requests` (>= 2.31.0): Handles secure server-side HTTP calls to LLM APIs without bulky SDK overhead.

---

### Step 4: Run the Application

Start the Flask development server:

```powershell
python app.py
```

You will see the startup banner in your terminal:
```text
=================================================================
[MOCK INTERVIEW AGENT] Computer Engineering College Project
Server running at: http://127.0.0.1:5000
Current Mode: Demo Mode (Offline / Rule-Based)
Notice: Demo Mode active. Set GEMINI_API_KEY in .env to enable real AI.
=================================================================
```

---

### Step 5: Open in Your Browser

Open your web browser (Chrome, Edge, Firefox, Brave) and go to:
👉 **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---

## 🧪 Running Automated Tests

To verify that all routes, scoring heuristics, question progressions, and final report generation are functioning correctly:

```powershell
python test_workflow.py
```

Expected output:
```text
============================================================
[TEST SUITE] Running Tests for Mock Interview Agent...
============================================================
[Test 1] Testing GET / (Home Page)...               [PASS]
[Test 2] Testing GET /api/status...                 [PASS]
[Test 3] Testing POST /api/start-session...         [PASS]
[Test 4] Testing Answer Submission (Thorough)...    [PASS]
[Test 5] Progressing through Questions 2-5...       [PASS]
[Test 6] Finalizing Session and Generating Report...[PASS]
[Test 7] Custom Role & Early End Interview...       [PASS]
[Test 8] Testing Edge Cases (Empty/Short Answers)...[PASS]
============================================================
[SUCCESS] ALL 8 TESTS PASSED COMPLETELY!
============================================================
```

---

## 🔑 Activating Real AI Mode (Google Gemini Free Tier)

By default, the application runs in **Demo Mode**, so you can present the project anytime without internet or API keys.

To enable live, real-time AI generation and grading using Google Gemini:

1. **Get a Free API Key**:
   - Go to [Google AI Studio](https://aistudio.google.com/).
   - Sign in with your Google account and click **Get API key** → **Create API key**.
2. **Add to `.env`**:
   - Open the `.env` file in the project folder.
   - Set your key:
     ```env
     GEMINI_API_KEY=AIzaSyYourGeneratedApiKeyHere
     GEMINI_MODEL=gemini-1.5-flash
     ```
3. **Restart the Server**:
   ```powershell
   python app.py
   ```
4. Refresh your browser! The status badge in the header will turn **green** (`AI-Powered Mode (Google Gemini)`).

> **Security Guarantee**: The API key is stored only on your computer inside `.env`. It is loaded by Flask on the server and is never sent to the client browser.

---

## 🎓 College Viva & Project Defense Guide

When presenting this project for your Computer Engineering third-year viva, faculty and external examiners often ask specific technical questions. Here are key answers:

### Q1: Why did you choose Python Flask over Django or Node.js?
> **Answer**: *"Flask is a micro-framework that adheres to the Single Responsibility Principle. For a mock interview agent requiring RESTful JSON endpoints and modular session handling, Flask provides minimal overhead, zero boilerplate, and fast execution without the heavy ORM and database overhead of Django, making it ideal for high-throughput AI middleware."*

### Q2: How does the application evaluate answers when in Demo Mode?
> **Answer**: *"In Demo Mode, `interview_engine.py` implements a multi-dimensional heuristic evaluation algorithm. It parses the candidate's answer into word and token streams, evaluates conceptual depth against curated domain keywords, detects structural indicators (like comparison words or the STAR method for HR questions), and dynamically calibrates the 10-point score, reasoning, strengths, and targeted improvement suggestions based on the chosen difficulty level."*

### Q3: How do you ensure API keys are protected?
> **Answer**: *"We strictly implement server-side credential isolation. API keys are stored in a local `.env` file that is excluded from version control via `.gitignore`. The frontend makes standard JSON REST calls to our Flask server, which performs the external API requests. The browser never receives or handles the private credentials."*

### Q4: How is interview session state managed?
> **Answer**: *"Each session is assigned a unique UUID (version 4) upon initialization. In the Flask backend, sessions are stored in memory with indices tracking the current question, candidate answers, individual evaluations, timestamps, and aggregate score tallies. This ensures lightweight, fast operations without database bottlenecks."*

### Q5: What happens if the external LLM API experiences rate limits or network latency?
> **Answer**: *"The system includes an automatic graceful fallback mechanism. If an external API call times out or returns an error, the engine catches the exception, logs it, and falls back to the deterministic rule-based evaluator. This guarantees that a student's live interview session is never interrupted or crashed during an assessment."*

---

## 📄 License & Academic Integrity

This project is created for educational and academic purposes as part of the **Third-Year Computer Engineering** curriculum. All rights reserved.
