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

### 6. Reviewing and Staging Files

- `git add`: stages selected files for a future commit.
- `git diff --cached --stat`: summarises staged changes.
- `git status`: verifies which files are staged.

**Why:** Reviewing staged files helps prevent accidental commits of private data or unwanted files.

**Status:** Files staged and reviewed; initial commit pending.

### 7. First Git Commit

- `git commit -m "Initialise Bookify project"`: saves the staged files as the first snapshot in Git history.
- `git log -1 --oneline`: displays the latest commit in a compact format.

**Why:** Commits create checkpoints that let us track progress and understand how the project evolves.

**Result:** Bookify's initial project setup and documentation are saved in Git.

### 8. Verifying the First Commit

- Commit created successfully: `ee39f2d`.
- `git status` revealed that the journal had changed after the commit.
- `git log -1 --oneline` confirmed the latest commit.

**What I learned:** Git commits preserve snapshots of staged files. Editing a file after a commit creates a new change that must be staged and committed separately.

**Result:** The initial project setup is saved, and the journal records the next step in the workflow.

### 9. Building the First Backend

- Created a Python virtual environment using `python -m venv .venv`.
- Installed FastAPI and its standard dependencies.
- Created `backend/Main.py` with a root endpoint and a health-check endpoint.
- Started the development server using Uvicorn.

**Concepts learned:**
- A backend processes requests and returns responses.
- An API defines how different parts of an application communicate.
- An endpoint is a URL that performs a specific function.
- A virtual environment isolates project dependencies.

**Verification:** Tested the root endpoint, health endpoint and interactive API documentation.

**Next step:** Add local PDF upload and text extraction.

### 10. Python Interpreter and Virtual Environments

- PyCharm reported that no Python interpreter was enabled.
- Created a virtual environment through PyCharm.
- Found two `.venv` folders in the project.
- Decided to use the root-level `.venv` as the project's main Python environment.

**What I learned:** A Python interpreter executes Python code. A virtual environment provides an isolated interpreter and project-specific packages.

**Next step:** Configure the project interpreter and verify the environment before installing backend dependencies.

### 11. Configuring the Python Interpreter

- Selected a project virtual environment in PyCharm.
- Verified Python 3.12.3 using `python.exe --version`.
- Confirmed that the virtual environment activates in the terminal.

**What I learned:** The terminal's `(.venv)` prefix indicates an activated virtual environment. Packages installed through that environment's Python belong to that environment.

**Next step:** Verify FastAPI installation and run Bookify's first backend endpoint.

### 12. Understanding Project Paths and Environments

- The terminal was inside the `backend` directory.
- FastAPI was installed in `backend/.venv`.
- The project also has a root-level `.venv`.

**What I learned:** The current working directory determines where relative paths point. A virtual environment determines which Python interpreter and installed packages are used.

**Decision:** Standardise on the root `.venv` to avoid managing two environments.

### 13. Standardising the Python Environment

- Deactivated the backend virtual environment.
- Returned to the project root using `cd ..`.
- Verified that the root `.venv` runs Python 3.12.3.
- Chose the root `.venv` as Bookify's single development environment.

**What I learned:** Python packages are installed separately in each virtual environment. The working directory also affects how Python imports project modules.

**Next step:** Run and verify the FastAPI backend from the project root.

### 14. End-of-Day Checkpoint

**Completed**
- Set up the local Git repository.
- Created the initial commit and documented basic Git commands.
- Verified Python 3.12.3 in the root virtual environment.
- Created the initial backend file and began configuring FastAPI.

**Still pending**
- Standardise on the root `.venv`.
- Verify FastAPI in the root environment.
- Run and test the first backend endpoint.
- Connect the local Git repository to GitHub.

**What I learned:** Git saves local snapshots through commits. GitHub can host a remote copy of the repository, but the connection must be configured separately.

**Next session:** Verify the environment, run the backend, and complete the GitHub setup.

### 15. First Backend Startup and Debugging

- Started Uvicorn from the project root.
- Encountered an error because the expected `app` attribute was not found in `backend.Main`.
- Checked that `Main.py` defines `app = FastAPI(...)` and saved the file.

**What I learned:** Uvicorn uses the format `module:variable` to locate an application. In `backend.Main:app`, `backend.Main` identifies the Python module and `app` identifies the FastAPI instance.

**Result:** Pending successful restart and endpoint verification.

### 16. First Backend Endpoint Successfully Tested

- Started the FastAPI application using Uvicorn.
- Fixed the missing `app` attribute issue in `backend.Main`.
- Tested `/` and confirmed the Bookify welcome response.
- Tested `/health` and confirmed the `ok` status.

**What I learned:** An API endpoint receives a request and returns a response. The health endpoint lets us check whether the backend is responding.

**Result:** Bookify's first backend endpoints are working locally.

**Next milestone:** Build the PDF upload and text extraction pipeline.