# 🐍 Vetlog Buddy


![Under Construction](https://img.shields.io/badge/status-wip-yellow?style=flat-square)
[![All Contributors](https://img.shields.io/badge/all_contributors-3-orange.svg?style=flat-square)](#contributors-)
[![GitHub](https://github.com/josdem/py-vetlog-analyzer/actions/workflows/main.yml/badge.svg)](https://github.com/josdem/py-vetlog-analyzer/actions)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=josdem_py-vetlog-analyzer&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=josdem_py-vetlog-analyzer)

Python-based helper for [vetlog-spring-boot](https://github.com/josdem/vetlog-spring-boot) 🐶🐱

## Setup

**Prerequisites**

- [vetlog-spring-boot](https://github.com/josdem/vetlog-spring-boot)
- MySQL 8+
- Python 3.12+
- uv

**Installation**

1. Clone the repository

```sh
git clone https://github.com/josdem/py-vetlog-buddy
cd py-vetlog-buddy
```

2. Install dependencies

```sh
uv sync
```

## Usage

**Run**

```sh
# Filter invalid users
uv run filter

# Filter suspicious users
uv run suspicious

# Create vaccination records
uv run vaccines
```
**Test**

```sh
# Test everything
uv run pytest

# Test a specific file
uv run pytest tests/test_filter_username.py

# Test a matching keyword
uv run pytest -k vaccination
```

## 🚧 WIP

**Links**

- https://github.com/josdem/py-vetlog-analyzer/wiki
- https://github.com/josdem/py-vetlog-buddy/graphs/contributors
- https://github.com/josdem/vetlog-spring-boot
- https://pypi.org/project/py-vetlog-analyzer
