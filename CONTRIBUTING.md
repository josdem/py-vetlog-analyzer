# Contributing to 🐍Vetlog Buddy

Thank you for your interest in contributing to Vetlog Buddy! Your help is highly appreciated. This guide will walk you through
the setup process, development workflows, and best practices for contributing to the project.

---

## Project Setup

### Prerequisites

- [vetlog-spring-boot](https://github.com/josdem/vetlog-spring-boot)
- MySQL 8+
- Python 3.12+
- uv

---

## Running the Application

### 1. Clone the repository

```bash
git clone https://github.com/josdem/py-vetlog-buddy
cd py-vetlog-buddy
```

### 2. Install the dependencies

```sh
uv sync
```

### 3. (Optional) Verify installation

```sh
uv run version
```

---

## How to Contribute

1. **Get the repository**
   - If you are a **new contributor**: **Fork** the repository
   - If you already have **write access**: **Clone** the repository
2. **Create a feature branch**:
    ```bash
    git checkout -b feature/<Github-issue-ID>
    ```
3. **Make your changes**
4. **Commit using clear messages** (use [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) if
   possible)
    ```bash
    git commit -m "feat: add ability to update pet profile"
    ```
5. **Push and submit a Pull Request (PR)** against the `main` branch
6. In your PR:
    - Link any relevant issue (e.g. `Closes #652`)
    - Provide a short summary of your changes

---

## Testing

```sh
# Run unit tests
uv run pytest tests/unit -v

# Test a specific file
uv run pytest tests/test_filter_username.py

# Test a matching keyword
uv run pytest -k vaccination
```
---

## Code Style & Linting

```sh
# Check code for linting/formatting issues (does not fix)
uv run ruff check

# Format code automatically
uv run ruff format

# Automatically fix linting issues
uv run ruff check --fix
```

_Format your code before pusing commits._

---

Thank you for contributing to 🐍Vetlog Buddy!️