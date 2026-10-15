/**
 * Mock Interview Agent - Frontend Application Script
 * Third-Year Computer Engineering College Project
 */

// Application State
const state = {
  sessionId: null,
  currentQuestionNumber: 1,
  totalQuestions: 5,
  timerInterval: null,
  secondsElapsed: 0,
  isSubmitting: false,
  role: "Java Developer",
  interviewType: "Technical",
  difficulty: "Beginner"
};

// DOM Content Loaded Handler
document.addEventListener("DOMContentLoaded", () => {
  fetchEngineStatus();
  setupEventListeners();
});

/**
 * Attaches header button listeners and keyboard shortcuts
 */
function setupEventListeners() {
  const statusBtn = document.getElementById("engine-status-btn");
  if (statusBtn) {
    statusBtn.addEventListener("click", openStatusModal);
  }

  // Ctrl+Enter / Cmd+Enter to submit answer inside textarea
  const textarea = document.getElementById("answer-textarea");
  if (textarea) {
    textarea.addEventListener("keydown", (e) => {
      if ((e.ctrlKey || e.metaKey) && e.key === "Enter") {
        e.preventDefault();
        const submitBtn = document.getElementById("submit-answer-btn");
        if (submitBtn && !submitBtn.disabled && !state.isSubmitting) {
          submitCurrentAnswer();
        }
      }
    });
  }
}

/**
 * Fetches engine status from backend API to update badge and banner
 */
async function fetchEngineStatus() {
  try {
    const res = await fetch("/api/status");
    const json = await res.json();
    if (json.success && json.data) {
      const data = json.data;
      const statusBtn = document.getElementById("engine-status-btn");
      const statusText = document.getElementById("engine-status-text");
      const alertBanner = document.getElementById("mode-alert-banner");
      const bannerText = document.getElementById("banner-notice-text");

      if (statusBtn && statusText) {
        statusText.textContent = data.mode_label;
        statusBtn.className = `status-badge ${data.badge_color}`;
      }

      if (alertBanner && bannerText) {
        alertBanner.className = `alert-banner ${data.mode}`;
        bannerText.textContent = data.notice;
      }
    }
  } catch (err) {
    console.warn("Could not fetch status update:", err);
  }
}

/**
 * Toggles visibility of custom role text input when 'Other' is chosen
 */
function toggleCustomRoleInput(show) {
  const wrapper = document.getElementById("custom-role-wrapper");
  const input = document.getElementById("custom-role-input");
  if (wrapper) {
    if (show) {
      wrapper.classList.remove("hidden");
      if (input) input.focus();
    } else {
      wrapper.classList.add("hidden");
    }
  }
}

/**
 * Starts interview session by collecting config and calling backend
 */
async function startInterviewSession() {
  const roleRadio = document.querySelector('input[name="role"]:checked');
  const typeRadio = document.querySelector('input[name="interview_type"]:checked');
  const diffRadio = document.querySelector('input[name="difficulty"]:checked');
  const customRoleInput = document.getElementById("custom-role-input");

  const role = roleRadio ? roleRadio.value : "Java Developer";
  const customRole = customRoleInput ? customRoleInput.value.trim() : "";
  const interviewType = typeRadio ? typeRadio.value : "Technical";
  const difficulty = diffRadio ? diffRadio.value : "Beginner";

  state.role = (role === "Other" && customRole) ? customRole : role;
  state.interviewType = interviewType;
  state.difficulty = difficulty;

  const startBtn = document.getElementById("start-btn");
  if (startBtn) {
    startBtn.disabled = true;
    startBtn.innerHTML = `
      <span class="btn-spinner"></span>
      <span>Initializing Interview...</span>
    `;
  }

  try {
    const response = await fetch("/api/start-session", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        role: role,
        custom_role: customRole,
        interview_type: interviewType,
        difficulty: difficulty
      })
    });

    const result = await response.json();
    if (!result.success) {
      alert("Failed to start session: " + (result.error || "Unknown server error"));
      if (startBtn) {
        startBtn.disabled = false;
        startBtn.innerHTML = `<span>Start Interview Session</span>`;
      }
      return;
    }

    const sessionData = result.data;
    state.sessionId = sessionData.session_id;
    state.currentQuestionNumber = sessionData.question_number || 1;
    state.totalQuestions = sessionData.total_questions || 5;

    // Transition view
    showView("view-interview");

    // Populate Interview UI
    updateInterviewHeader(sessionData);
    displayQuestion(sessionData);

    // Reset and start timer
    startSessionTimer();

  } catch (err) {
    alert("Connection error: Unable to contact the Flask backend. Please ensure the server is running.");
    console.error(err);
  } finally {
    if (startBtn) {
      startBtn.disabled = false;
      startBtn.innerHTML = `
        <span>Start Interview Session</span>
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <line x1="5" y1="12" x2="19" y2="12"></line>
          <polyline points="12 5 19 12 12 19"></polyline>
        </svg>
      `;
    }
  }
}

/**
 * Updates interview header tags (Role, Type, Difficulty)
 */
function updateInterviewHeader(data) {
  const roleTag = document.getElementById("meta-role-tag");
  const typeTag = document.getElementById("meta-type-tag");
  const diffTag = document.getElementById("meta-difficulty-tag");

  if (roleTag) roleTag.textContent = data.role;
  if (typeTag) typeTag.textContent = data.interview_type;
  if (diffTag) diffTag.textContent = data.difficulty;
}

/**
 * Displays a new question in the interview card
 */
function displayQuestion(data) {
  const qNum = data.question_number || state.currentQuestionNumber;
  const total = data.total_questions || state.totalQuestions;

  // Progress update
  const progressText = document.getElementById("progress-text");
  const progressPct = document.getElementById("progress-percentage");
  const progressFill = document.getElementById("progress-fill");

  const pct = Math.round((qNum / total) * 100);
  if (progressText) progressText.textContent = `Question ${qNum} of ${total}`;
  if (progressPct) progressPct.textContent = `${pct}% Completed`;
  if (progressFill) progressFill.style.width = `${pct}%`;

  // Question Card details
  const categoryBadge = document.getElementById("question-category");
  const qNumPill = document.getElementById("question-number-pill");
  const questionText = document.getElementById("question-text");

  if (categoryBadge) categoryBadge.textContent = data.category || "Core Engineering";
  if (qNumPill) qNumPill.textContent = `Question #${qNum}`;
  if (questionText) questionText.textContent = data.question;

  // Reset textarea & counters
  const textarea = document.getElementById("answer-textarea");
  if (textarea) {
    textarea.value = "";
    textarea.disabled = false;
    textarea.focus();
  }
  updateAnswerStats();

  // Hide feedback card and restore submit button
  const feedbackCard = document.getElementById("feedback-card");
  if (feedbackCard) feedbackCard.classList.add("hidden");

  const submitBtn = document.getElementById("submit-answer-btn");
  if (submitBtn) {
    submitBtn.classList.remove("hidden");
    submitBtn.disabled = false;
  }
}

/**
 * Live character and word count tracking
 */
function updateAnswerStats() {
  const textarea = document.getElementById("answer-textarea");
  const wordBadge = document.getElementById("word-count-badge");
  const charBadge = document.getElementById("char-count-badge");

  if (!textarea) return;

  const text = textarea.value.trim();
  const words = text ? text.split(/\s+/).filter(Boolean) : [];
  const wordCount = words.length;
  const charCount = textarea.value.length;

  if (wordBadge) wordBadge.textContent = `${wordCount} word${wordCount === 1 ? '' : 's'}`;
  if (charBadge) charBadge.textContent = `${charCount} character${charCount === 1 ? '' : 's'}`;
}

/**
 * Submits the student's answer for evaluation
 */
async function submitCurrentAnswer() {
  if (state.isSubmitting) return;

  const textarea = document.getElementById("answer-textarea");
  const answer = textarea ? textarea.value.trim() : "";

  if (!answer) {
    const confirmEmpty = confirm("Your answer box is currently empty. Would you like to submit an empty answer? (In an interview, submitting an empty response receives 0 points)");
    if (!confirmEmpty) {
      if (textarea) textarea.focus();
      return;
    }
  }

  const submitBtn = document.getElementById("submit-answer-btn");
  const submitSpinner = document.getElementById("submit-spinner");
  const submitBtnText = document.getElementById("submit-btn-text");

  state.isSubmitting = true;
  if (submitBtn) submitBtn.disabled = true;
  if (submitSpinner) submitSpinner.classList.remove("hidden");
  if (submitBtnText) submitBtnText.textContent = "Analyzing Answer...";

  try {
    const response = await fetch("/api/submit-answer", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        session_id: state.sessionId,
        answer: answer
      })
    });

    const result = await response.json();
    if (!result.success) {
      alert("Error submitting answer: " + (result.error || "Unknown error"));
      return;
    }

    const data = result.data;
    renderFeedback(data);

    // Disable textarea after submission
    if (textarea) textarea.disabled = true;
    if (submitBtn) submitBtn.classList.add("hidden");

  } catch (err) {
    alert("Connection error: Unable to submit answer. Please check if your server is running.");
    console.error(err);
  } finally {
    state.isSubmitting = false;
    if (submitSpinner) submitSpinner.classList.add("hidden");
    if (submitBtnText) submitBtnText.textContent = "Submit Answer";
  }
}

/**
 * Displays feedback card with scores, strengths, areas to improve, and sample answer
 */
function renderFeedback(data) {
  const evalData = data.evaluation;
  const isLast = data.is_last_question;

  const feedbackCard = document.getElementById("feedback-card");
  const scoreVal = document.getElementById("feedback-score-val");
  const scoreCircle = document.getElementById("score-circle");
  const scoreReason = document.getElementById("feedback-score-reason");
  const evalMode = document.getElementById("feedback-eval-mode");
  const strengthsList = document.getElementById("feedback-strengths-list");
  const improvementsList = document.getElementById("feedback-improvements-list");
  const sampleAnswer = document.getElementById("feedback-sample-answer");
  const nextBtnText = document.getElementById("next-btn-text");

  if (!feedbackCard || !evalData) return;

  // Score value & styling
  const score = parseFloat(evalData.score);
  if (scoreVal) scoreVal.textContent = evalData.score.toFixed(1);

  if (scoreCircle) {
    scoreCircle.className = "score-circle";
    if (score >= 7.5) scoreCircle.classList.add("green");
    else if (score >= 5.0) scoreCircle.classList.add("amber");
    else scoreCircle.classList.add("red");
  }

  // Reason & mode
  if (scoreReason) scoreReason.textContent = evalData.reason;
  if (evalMode) evalMode.textContent = evalData.mode_used || "Standard Evaluation";

  // Strengths
  if (strengthsList) {
    strengthsList.innerHTML = "";
    (evalData.strengths || []).forEach(item => {
      const li = document.createElement("li");
      li.textContent = item;
      strengthsList.appendChild(li);
    });
  }

  // Areas to improve
  if (improvementsList) {
    improvementsList.innerHTML = "";
    (evalData.areas_to_improve || []).forEach(item => {
      const li = document.createElement("li");
      li.textContent = item;
      improvementsList.appendChild(li);
    });
  }

  // Sample answer
  if (sampleAnswer) {
    sampleAnswer.textContent = evalData.sample_answer || "No sample answer available.";
  }

  // Next Button Label (Next Question vs View Final Report)
  if (nextBtnText) {
    nextBtnText.textContent = isLast ? "View Final Report 🎉" : "Next Question";
  }

  // Reveal card and scroll smoothly
  feedbackCard.classList.remove("hidden");
  feedbackCard.scrollIntoView({ behavior: "smooth", block: "start" });
}

/**
 * Advances to the next question or finishes the interview
 */
async function advanceNextQuestion() {
  const nextBtn = document.getElementById("next-question-btn");
  const nextSpinner = document.getElementById("next-spinner");
  const nextText = document.getElementById("next-btn-text");

  if (nextBtn) nextBtn.disabled = true;
  if (nextSpinner) nextSpinner.classList.remove("hidden");

  try {
    const response = await fetch("/api/next-question", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ session_id: state.sessionId })
    });

    const result = await response.json();
    if (!result.success) {
      alert("Error: " + (result.error || "Could not proceed to next question"));
      return;
    }

    const data = result.data;
    if (data.has_next) {
      state.currentQuestionNumber = data.question_number;
      displayQuestion(data);
      window.scrollTo({ top: 0, behavior: "smooth" });
    } else {
      // Completed! Show final report
      stopSessionTimer();
      renderFinalReport(data.report);
      showView("view-report");
      window.scrollTo({ top: 0, behavior: "smooth" });
    }

  } catch (err) {
    alert("Connection error: Unable to load next question.");
    console.error(err);
  } finally {
    if (nextBtn) nextBtn.disabled = false;
    if (nextSpinner) nextSpinner.classList.add("hidden");
  }
}

/**
 * Triggers modal to confirm early termination of interview
 */
function confirmEndInterview() {
  const modal = document.getElementById("confirm-end-modal");
  if (modal) modal.classList.remove("hidden");
}

function closeConfirmModal() {
  const modal = document.getElementById("confirm-end-modal");
  if (modal) modal.classList.add("hidden");
}

/**
 * Executes early termination and fetches current session report
 */
async function executeEndInterview() {
  closeConfirmModal();
  stopSessionTimer();

  try {
    const response = await fetch("/api/end-session", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ session_id: state.sessionId })
    });

    const result = await response.json();
    if (result.success && result.data && result.data.report) {
      renderFinalReport(result.data.report);
      showView("view-report");
      window.scrollTo({ top: 0, behavior: "smooth" });
    } else {
      alert("Error ending session: " + (result.error || "Unknown error"));
    }
  } catch (err) {
    alert("Connection error while ending session.");
    console.error(err);
  }
}

/**
 * Renders the final performance report scorecard & history
 */
function renderFinalReport(report) {
  if (!report) return;

  const metaSubtitle = document.getElementById("report-meta-subtitle");
  const avgScore = document.getElementById("report-avg-score");
  const totalScore = document.getElementById("report-total-score");
  const questionsCount = document.getElementById("report-questions-count");
  const verdict = document.getElementById("report-verdict");
  const verdictDesc = document.getElementById("report-verdict-desc");
  const strengthsList = document.getElementById("report-strengths-list");
  const improvementsList = document.getElementById("report-improvements-list");
  const historyContainer = document.getElementById("report-history-container");

  if (metaSubtitle) {
    metaSubtitle.textContent = `Role: ${report.role} • Type: ${report.interview_type} • Difficulty: ${report.difficulty}`;
  }

  if (avgScore) avgScore.textContent = `${report.average_score.toFixed(1)} / 10`;
  if (totalScore) totalScore.textContent = `${report.total_score.toFixed(1)} / ${report.max_possible_score}`;
  if (questionsCount) questionsCount.textContent = `${report.questions_answered} of ${report.total_questions}`;
  
  if (verdict) {
    const avg = report.average_score;
    if (avg >= 8.5) verdict.textContent = "Outstanding Performance";
    else if (avg >= 7.0) verdict.textContent = "Strong Performance";
    else if (avg >= 5.0) verdict.textContent = "Developing Potential";
    else verdict.textContent = "Needs Revision";
  }

  if (verdictDesc) {
    verdictDesc.textContent = report.performance_verdict;
  }

  // Consolidated Strengths
  if (strengthsList) {
    strengthsList.innerHTML = "";
    (report.consolidated_strengths || []).forEach(s => {
      const li = document.createElement("li");
      li.textContent = s;
      strengthsList.appendChild(li);
    });
    if (!report.consolidated_strengths || report.consolidated_strengths.length === 0) {
      const li = document.createElement("li");
      li.textContent = "No specific strengths recorded yet.";
      strengthsList.appendChild(li);
    }
  }

  // Consolidated Improvements
  if (improvementsList) {
    improvementsList.innerHTML = "";
    (report.consolidated_improvements || []).forEach(imp => {
      const li = document.createElement("li");
      li.textContent = imp;
      improvementsList.appendChild(li);
    });
    if (!report.consolidated_improvements || report.consolidated_improvements.length === 0) {
      const li = document.createElement("li");
      li.textContent = "Continue practicing full-length mock interviews to maintain your consistency.";
      improvementsList.appendChild(li);
    }
  }

  // Build Interview History Accordion / List
  if (historyContainer) {
    historyContainer.innerHTML = "";
    const history = report.history || [];

    if (history.length === 0) {
      historyContainer.innerHTML = `<p class="hint-text">No questions were answered during this session.</p>`;
      return;
    }

    history.forEach((item, idx) => {
      const itemEl = document.createElement("div");
      itemEl.className = "history-item";

      const scoreNum = parseFloat(item.score);
      let pillClass = "green";
      if (scoreNum < 5.0) pillClass = "red";
      else if (scoreNum < 7.5) pillClass = "amber";

      itemEl.innerHTML = `
        <div class="history-item-header" onclick="toggleHistoryDetails('history-body-${idx}')">
          <div class="history-item-title">
            <span class="history-q-num">Q${item.question_number}</span>
            <span>${escapeHtml(item.question)}</span>
          </div>
          <span class="history-score-pill ${pillClass}">${item.score_display}</span>
        </div>

        <div class="history-item-body" id="history-body-${idx}">
          <div class="history-field">
            <div class="history-field-label">Candidate Answer</div>
            <div class="history-field-text">${item.answer ? escapeHtml(item.answer) : '<em>(No response provided)</em>'}</div>
          </div>

          <div class="history-field">
            <div class="history-field-label">Evaluation Reason</div>
            <div class="history-field-text">${escapeHtml(item.reason)}</div>
          </div>

          <div class="history-field">
            <div class="history-field-label">Exemplary Model Answer</div>
            <div class="history-field-text history-sample-text">${escapeHtml(item.sample_answer)}</div>
          </div>
        </div>
      `;

      historyContainer.appendChild(itemEl);
    });
  }
}

/**
 * Toggles accordion body in history view
 */
function toggleHistoryDetails(elementId) {
  const el = document.getElementById(elementId);
  if (el) {
    el.classList.toggle("hidden");
  }
}

/**
 * Resets state back to home/setup view
 */
function resetToSetupView() {
  state.sessionId = null;
  state.currentQuestionNumber = 1;
  state.secondsElapsed = 0;
  stopSessionTimer();

  // Reset inputs
  const textarea = document.getElementById("answer-textarea");
  if (textarea) textarea.value = "";

  showView("view-setup");
  window.scrollTo({ top: 0, behavior: "smooth" });
}

/**
 * Switches active view
 */
function showView(viewId) {
  document.querySelectorAll(".view-section").forEach(sec => {
    sec.classList.remove("active");
  });
  const target = document.getElementById(viewId);
  if (target) target.classList.add("active");
}

/**
 * Timer tracking for interview session
 */
function startSessionTimer() {
  stopSessionTimer();
  state.secondsElapsed = 0;
  updateTimerDisplay();

  state.timerInterval = setInterval(() => {
    state.secondsElapsed++;
    updateTimerDisplay();
  }, 1000);
}

function stopSessionTimer() {
  if (state.timerInterval) {
    clearInterval(state.timerInterval);
    state.timerInterval = null;
  }
}

function updateTimerDisplay() {
  const display = document.getElementById("session-timer-display");
  if (!display) return;

  const mins = Math.floor(state.secondsElapsed / 60);
  const secs = state.secondsElapsed % 60;
  const formatted = `⏱️ ${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
  display.textContent = formatted;
}

/**
 * Modal handlers for status & setup guide
 */
function openStatusModal() {
  const modal = document.getElementById("status-modal");
  if (modal) modal.classList.remove("hidden");
}

function closeStatusModal() {
  const modal = document.getElementById("status-modal");
  if (modal) modal.classList.add("hidden");
}

/**
 * Utility to escape HTML and prevent XSS
 */
function escapeHtml(str) {
  if (!str) return "";
  return str
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}
