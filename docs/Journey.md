# Bookify: Development Journey

## Session 01: Environment Setup

**Date:** 27 October 2026

### Objective
Prepare the development environment for Bookify, a personal knowledge discovery application built around books, playlists and cross-source learning.

### Environment
- Operating system: Windows
- IDE: JetBrains PyCharm
- Python: 3.12.3
- Git: 2.55.0
- Node.js: 24.22.0
- npm: 11.19.1

### What I learned
- Python and Node.js are separate runtimes used for different parts of the application.
- Git tracks changes to source code and documentation.
- PowerShell can block `.ps1` scripts according to its execution policy.
- Using `npm.cmd` lets me run npm commands without changing that policy.

### Decisions
- Use Python and FastAPI for the backend.
- Use React and Vite for the frontend.
- Store application metadata in SQLite and uploaded PDFs on the local filesystem.
- Document implementation decisions, debugging and concepts as the project evolves.

### Next milestone
Create the initial project structure, initialise Git, and build a working backend health endpoint.

### Verification
Python, Git, Node.js and npm version commands completed successfully.


## Session 02: Project Setup and Git Basics

### 1. Environment Setup

Verified the installed development tools:

- `python --version`: checks the installed Python version.
- `git --version`: checks the installed Git version.
- `node --version`: checks the installed Node.js version.
- `npm.cmd --version`: checks npm without triggering PowerShell's script restriction.

### 2. Project Structure

Created folders for the backend, frontend, local data, documentation and tests.

**Why:** Separating components makes the project easier to maintain as it grows.

### 3. Git Setup

- `git init`: initialises Git in the project folder.
- `git status`: shows the current repository state and untracked files.
- `git config user.name`: checks the name attached to commits.
- `git config user.email`: checks the email attached to commits.

**Key concept:** Git tracks changes to files over time. A commit is a saved snapshot of selected changes.

### 4. Git Ignore Rules

Created `.gitignore` to exclude virtual environments, API keys, local databases, uploaded PDFs, generated files and IDE settings.

**Why:** These files are unnecessary for sharing the source code and may contain private information.

### 5. Current Status

- Git repository initialised.
- Git username and email configured.
- Project folders created.
- `.gitignore` created.
- Initial commit still pending.

### Next Step

Check `git status`, inspect the files to be tracked, and create the first commit.