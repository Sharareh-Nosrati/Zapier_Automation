# Zapier Automation – AI Lead Qualification Workflow

## What this is
This folder documents a Zapier-based automation system used to
qualify inbound restaurant leads using rule-based logic and AI assistance.

The system was designed to support Sales and Marketing teams
with fast, explainable lead handling.

---

## How data enters the system
Leads enter through a Google Form filled by potential restaurant customers.

The form collects:
- restaurant name
- city
- lead source
- customer interest/actions
- contact email

Each submission triggers the main automation.

---

## Core automation (AI Lead Workflow)
The main Zap performs the following steps:

1. Stores the lead in Google Sheets (acting as a lightweight CRM)
2. Generates a unique lead identifier
3. Applies deterministic scoring using Python
4. Classifies lead quality (low / medium / high)
5. Uses OpenAI to generate a structured internal summary
6. Updates the CRM sheet with AI outputs
7. Sends Slack alerts for high-quality leads

---

## Lead scoring logic
Lead scoring is rule-based and transparent.
Each customer action contributes to a numeric score.

This logic is implemented using Python inside Zapier
to ensure explainability and business control.

---

## AI usage
OpenAI is used for:
- Summarizing lead context
- Suggesting next actions
- Explaining lead quality in natural language

AI is constrained to:
- provided data only
- structured outputs
- no hallucinated facts

---

## Slack interaction (Ask Why)
When a lead is posted in Slack, team members can ask questions
such as “Why is this lead high?”.

The system retrieves the related lead data and
responds inside the same thread with a clear explanation.

This enables fast decision-making without dashboards.

---

## Customer communication
A separate automation sends a confirmation email to the lead.

This email:
- is customer-safe
- contains no internal scoring
- reassures the lead that the request was received

---

## Design rationale
The system prioritizes:
- explainability over black-box automation
- human-in-the-loop decision making
- low operational complexity
