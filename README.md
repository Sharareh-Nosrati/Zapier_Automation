# Zapier Automation – AI Lead Qualification Workflow

## Overview
This Zapier workflow orchestrates the end-to-end handling of inbound leads:
from form submission, to scoring, to internal Slack alerts, to customer email confirmation.

The focus is on **explainable decision logic** and **human-in-the-loop interaction**,
not black-box automation.

---

## High-level Flow

Google Form  
→ Zapier  
→ Google Sheets (CRM table)  
→ Rule-based scoring (Python)  
→ OpenAI (summary + explanation)  
→ Slack alerts + threaded Q&A  
→ Customer confirmation email

---

## Trigger
- **Google Form – New Form Response**
- Collects:
  - name
  - restaurant name
  - city
  - source
  - actions / interest
  - contact email (validated)

---

## Data Storage
- Leads are stored in **Google Sheets** acting as a lightweight CRM
- Each lead is assigned a unique `lead_id`
- This ID is used to connect Slack messages, AI explanations, and CRM rows

---

## Lead Scoring Logic
- Implemented using **Code by Zapier (Python)**
- Deterministic, rule-based scoring
- Outputs:
  - score
  - lead_quality (low / medium / high)
  - owner_team
  - next_step

Scoring is transparent and explainable.

---

## AI Usage
OpenAI is used for:
- Internal lead summaries
- Suggested next steps
- Slack-based explanations (e.g. “Why is this lead high?”)
- Customer-facing confirmation emails (separate prompt, no internal data leakage)

AI is constrained to:
- provided lead data only
- no hallucination
- structured outputs

---

## Slack Integration
- High-quality leads are posted to a shared Slack channel
- Team members can reply in-thread with questions
- The system retrieves the correct lead via `lead_id`
- AI responds inside the same thread with a clear explanation

---

## Customer Email
- A confirmation email is sent automatically after form submission
- Email is customer-safe:
  - no scores
  - no internal logic
  - no AI mention
- Sent via **Email by Zapier**

---

## Notes on Deployment
This workflow is environment-specific (Zapier, Slack, API keys).
It is designed to be **recreated**, not shared as a live system.

Screenshots and logic are provided to demonstrate behavior and design.
