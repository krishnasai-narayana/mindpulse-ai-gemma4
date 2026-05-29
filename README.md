# MindPulse AI

## Overview

MindPulse AI is a Mental Wellness Assistant powered by Google Gemma 4 running locally through Ollama.

The application helps users assess:

* Stress Levels
* Anxiety Levels
* Burnout Risk
* Mood Consistency

while keeping all data private on the user's machine.

---

## Problem Statement

Mental stress, anxiety, and burnout are increasingly common. Many users lack quick and private tools to reflect on their emotional wellbeing.

MindPulse AI provides a simple interface where users can describe how they are feeling and receive personalized wellness insights.

---

## Gemma Usage

This project uses **Gemma 4 (gemma4:e4b)** via Ollama.

Gemma is responsible for:

* Emotional analysis
* Stress assessment
* Anxiety assessment
* Burnout detection
* Mood consistency evaluation
* Wellness recommendations

All inference runs locally.

---

## Features

### Mental Wellness Assessment

Users describe how they are feeling and receive:

* Stress Score
* Anxiety Score
* Burnout Score
* Summary
* Personalized Recommendations

### Mood Consistency Analysis

Users select their current mood and Gemma evaluates whether the written journal aligns with the selected emotional state.

### Privacy First

No data leaves the local machine.

### Wellness Report

Users can download a PDF wellness report generated from the assessment.

### Assessment History

Assessment scores are stored locally for future trend analysis.

---

## Tech Stack

* Python
* Streamlit
* Ollama
* Gemma 4
* ReportLab
* Pandas

---

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
streamlit run app.py
```

Ensure Ollama is running:

```bash
ollama run gemma4:e4b
```

---

## Future Enhancements

* Trend Visualization Dashboard
* Multi-session Wellness Tracking
* Personalized Wellness Plans
* Longitudinal Burnout Monitoring

---

## Author
Krishna Sai Narayana has built it for the Gemma 4 Buildathon.