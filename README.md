# Munazum

**Munazum** is a safe, deterministic folder organiser with an assistive
machine-learning layer.

It organises files by creating an **organised copy** of a selected folder.
Nothing is deleted, nothing is overwritten, and nothing happens silently.

> Munazum is opinionated about safety and explicitness.
> Automation is never trusted without visibility.

---

## ✨ Features

- Organise **one user-selected folder** at a time
- Deterministic, rule-based categorisation
- **Dry-run mode** (preview before doing anything)
- Creates an organised **copy**, originals stay untouched
- Assistive ML suggestions with **confidence scores**
- Local-only decision logging (no telemetry, no cloud)

---

## 🚫 What Munazum Will *Never* Do

- Delete files
- Overwrite existing files
- Modify files outside the selected folder
- Move files without an explicit plan
- Make silent “AI decisions”

---

## 🧠 About the Machine Learning

Munazum uses **assistive ML**, not automation.

- ML observes which decisions you approve
- Learns preferences from **local decision logs**
- Surfaces **suggestions only**
- Provides numeric confidence (explainable)
- Never overrides rules or executes actions

---

## 📦 Folder Categories (v0)

- documents (PDF, DOCX, TXT, etc.)
- code (Python, C/C++, JS, etc.)
- videos
- audios
- executables
- archives

---

## 🚀 Quick Start

From the project root:

### Dry run (recommended)
```bash
python -m munazum run . --dry-run
