# Tiny Journalctl Command Translator (TJCT)

TJCT is a minimal, deterministic helper module that converts structured
log queries into safe `journalctl` command strings.

It is designed to be used by an AI system or automation layer without
allowing command execution, shell access, or free-form input.

---

## 🎯 Purpose

- Translate log intent → valid `journalctl` command
- Prevent command injection
- Eliminate hallucinated flags
- Keep system access read-only

TJCT **does not execute commands**.

---

## 🧠 Design Philosophy

- Deterministic behavior
- Strict input validation
- No natural language generation
- No shell execution
- Small trusted surface area

This module is intentionally boring—and therefore safe.

---

## 📦 Features

- Time-based log queries (`X minutes/hours/days ago`)
- Optional service filtering (`-u service`)
- Optional priority filtering (`-p 0–7`)
- Optional kernel-only logs (`-k`)
- Always disables pager output

---

## 📥 Input Schema

TJCT accepts a single structured dictionary:

```json
{
  "type": "journal_query",
  "time": {
    "value": 2,
    "unit": "hours"
  },
  "service": null,
  "priority": null,
  "kernel": false
}