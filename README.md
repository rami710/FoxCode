# 🦊 FoxCode Engine

An ultra-fast, zero-dependency HTML generator and streaming compiler written in pure Python. Designed for instant live rendering and heavy stress testing.

---

### Overview
**FoxCode** is a lightweight, high-performance compiler engine that turns minimalist syntax and commands into clean HTML pages with automated browser previews. Built with an internal memory buffer and a universal fallback injector, it handles thousands of elements seamlessly without blocking the system.

### Key Features
* **Zero External Dependencies:** Built strictly with standard Python libraries (`os`, `webbrowser`).
* **Universal Raw Code Injector:** Any unmapped keyword or raw HTML/CSS/JS snippet is injected directly without runtime errors.
* **High-Performance Stress Testing:** Generate 5,000+ interactive elements or blocks in milliseconds.
* **Instant Live Browser Rendering:** The `totalpro` command compiles the buffer and opens your default browser immediately.

### Lexicon & Command Reference
| Command / Keyword | Description |
| :--- | :--- |
| `titre` / `h1` / `title` | Creates a main heading. |
| `texte` / `ecrire` / `print` | Creates a text paragraph. |
| `bouton` / `button` | Inserts a styled button. |
| `div` / `boite` | Creates a standard container block. |
| `generer_geant <N>` | Stress test: generates N blocks to benchmark performance. |
| `generer_boutons <N>` | Stress test: generates N styled interactive buttons. |
| `totalpro` / `run` / `build` | Compiles the buffer and launches the browser. |
| `reset` / `clear` | Clears the current buffer and resets the workspace. |

### Quick Start
1. Run the engine:
   ```bash
   python foxcode.py