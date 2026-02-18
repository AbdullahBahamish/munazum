Below is a corrected and refined `README.md`. Redundancies removed. Structure tightened. Tone professional and consistent.

---

```html
<!-- <p align="centre">
  <img src="assets/munazum-logo.png" alt="Munazum Logo" width="100%"/>
</p> -->

<h1 align="centre">Munazum</h1>

<p align="centre">
  <strong>A safe, intelligent CLI for organising real-world directories</strong>
</p>
```

---

## What is Munazum?

**Munazum** is a Python-based command-line tool that analyses and organises cluttered directories (e.g. Downloads) into a clean, predictable structure.

It combines deterministic file rules with assistive machine-learning suggestions while keeping the user fully in control through transparent logging and a strict dry-run mode.

No silent actions. No irreversible operations. No guesswork.

---

## Why Munazum?

Most file organisers either:

* operate blindly, or
* over-promise opaque “AI automation”.

Munazum prioritises:

* Visibility over automation
* Safety over speed
* Explainability over black-box behaviour

---

## How It Works

Munazum processes a directory in three stages:

1. **Scan**
   Recursively inspects files and subdirectories.

2. **Decide**
   Applies rule-based classification, optionally enhanced with confidence-scored ML suggestions.

3. **Execute (optional)**
   Copies files into a structured `Organized/` directory — only when explicitly permitted.

---

## Resulting Structure

```text
Organized/
├─ documents/
├─ archives/
├─ executables/
├─ videos/
├─ code/
└─ others/
```

Original files are never deleted or moved. They are copied only.

---

## Installation

```bash
git clone https://github.com/your-username/munazum.git
cd munazum
pip install -e .
```

Installed in editable mode for development and global CLI access.

---

## Usage

### Safe Preview (Recommended)

```bash
python -m munazum run . --dry-run
```

Displays planned operations without modifying the filesystem.

---

### Verbose Preview

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

### Execute Organisation

```bash
python -m munazum run .
```

Creates the `Organized/` directory and performs the planned copy operations.

---

## Safety Model

* Dry-run mode is strict
* No files or folders are created unless execution is confirmed
* All actions are logged
* No destructive operations by design

---

## Design Principles

* Conservative by default
* Transparent by design
* Modular and extensible
* Built for real-world directories

---

## Technical Stack

* Python 3.10+
* `pyproject.toml` packaging
* Editable installation via `pip`
* CLI module execution (`python -m munazum`)

---

## Author

Abdullah Bahamish
Computer Science student · AI & systems enthusiast

---

## License

MIT License

```
```
