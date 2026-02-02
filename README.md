# 🧠 AI Cognitive Load Auditor

> **An autonomous QA agent that quantifies "User Friction" using Multimodal AI.**

![Project Status](https://img.shields.io/badge/Status-Prototype-green)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Playwright](https://img.shields.io/badge/Tools-Playwright-orange)
![Gemini](https://img.shields.io/badge/AI-Google%20Gemini%20Vision-purple)

## 📋 Overview

Traditional QA automation (Selenium, Cypress) is excellent at catching **Functional Bugs** (e.g., "The button is broken"). However, it completely misses **Subjective Bugs** (e.g., "The button is invisible because of low contrast").

The **AI Cognitive Load Auditor** bridges this gap. It is an automated agent that:
1.  **Navigates** live web environments using a headless browser.
2.  **Perceives** the UI using Computer Vision (Google Gemini 1.5 Flash).
3.  **Analyzes** the interface for cognitive load, visual clutter, and UX friction.
4.  **Reports** actionable insights and a "Friction Score" (0-10) to a CSV file.

## 🚀 Key Features

* **Automated Visual Analysis:** No need for hard-coded selectors. The AI "looks" at the page like a human user.
* **Friction Scoring:** Assigns a quantitative score (0-10) to subjective user experience.
* **Competitor Benchmarking:** Can run against a suite of URLs to compare your site vs. competitors.
* **CSV Reporting:** Automatically generates a `ux_audit_report.csv` for stakeholder review.

## 🛠️ Tech Stack

* **Language:** Python
* **Browser Automation:** Playwright (Headless Chromium)
* **Artificial Intelligence:** Google Gemini Pro Vision API (via `google-generativeai`)
* **Data Handling:** Python `csv` and `os` libraries

## 💡 The "Why" (Market Gap)

In the current QA landscape, "Quality" is often synonymous with "Functionality." This tool introduces the concept of **"Quality Intelligence"**—moving beyond *checking* code to *evaluating* experience. By automating the discovery of bad UX, we reduce the reliance on expensive manual User Acceptance Testing (UAT) cycles.

---
**Built by Tanu Gupta**
*MSIST Candidate, Cybersecurity & Quality Assurance* , California State University, San Bernadino
