# 🗂️ Munazum

### *A safe, intelligent CLI for organising real-world folders*

<p align="center">
  <b>Turn chaos into structure — without risking your files.</b>
</p>

---

## 🚀 What is Munazum?

**Munazum** is a Python-based command-line tool that **analyses and organises cluttered directories** (such as your Downloads folder) into a clean, predictable structure.

It combines **deterministic file rules** with **assistive machine-learning suggestions**, while keeping the user fully in control through transparent logging and a strict dry-run mode.

No silent actions. No irreversible operations. No guesswork.

---

## ✨ Why Munazum?

Most file organisers either:

* act blindly, or
* over-promise “AI magic”

Munazum does neither.

It is built for users who value:

* 🔍 **Visibility** over automation
* 🛡️ **Safety** over speed
* 🧠 **Explainable decisions** over black boxes

---

## 🧠 How It Works

Munazum processes a directory in three stages:

1. **Scan**
   Recursively inspects files and folders.

2. **Decide**
   Applies rule-based classification, enhanced with confidence-scored ML suggestions.

3. **Execute (optional)**
   Copies files into a structured `Organized/` folder — *only if explicitly allowed*.

---

## 📁 Resulting Structure

```text
Organized/
├─ documents/
├─ archives/
├─ executables/
├─ videos/
├─ code/
└─ others/
```

Original files are **never deleted or moved** — only copied.

---

## 🛠️ Installation

```bash
git clone https://github.com/your-username/munazum.git
cd munazum
pip install -e .
```

Munazum is installed in **editable mode**, allowing global execution during development.

---

## ▶️ Usage

### 🔹 Safe Preview (Recommended)

```bash
python -m munazum run . --dry-run
```

> Shows what *would* happen — makes **zero filesystem changes**.

---

### 🔹 Full Transparency Mode

```bash
python -m munazum run . --dry-run --verbose
```

Example output:

```text
INFO: Target folder: C:\Users\USER\Downloads
INFO: Planned operations: 57
INFO: DRY-RUN: Copying report.pdf → Organized/documents/report.pdf
```

---

### 🔹 Real Execution

```bash
python -m munazum run .
```

> Executes the planned organisation and creates the `Organized/` folder.

---

## 🛡️ Safety First

* Dry-run mode is **strict**
* No folders or files are created unless permitted
* All operations are logged
* No destructive actions by design

Munazum assumes **user trust must be earned, not assumed**.

---

## 🧩 Design Principles

* **Conservative by default**
* **Transparent by design**
* **Modular and extensible**
* **Built for real folders, not demos**

---

## 📦 Technical Stack

* Python 3.10+
* `pyproject.toml` packaging
* Editable installs via `pip`
* CLI module execution (`python -m munazum`)

---

##    Author

**Abdullah Bahamish**

Computer Science student · AI & systems enthusiast

---

## 📄 License

MIT License
