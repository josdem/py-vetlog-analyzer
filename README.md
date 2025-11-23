# 🐍 Vetlog Buddy

<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->

![Under Construction](https://img.shields.io/badge/status-wip-yellow?style=flat-square)
[![All Contributors](https://img.shields.io/badge/all_contributors-3-orange.svg?style=flat-square)](#contributors-)
[![GitHub](https://github.com/josdem/py-vetlog-analyzer/actions/workflows/main.yml/badge.svg)](https://github.com/josdem/py-vetlog-analyzer/actions)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=josdem_py-vetlog-analyzer&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=josdem_py-vetlog-analyzer)

Python-based helper for [vetlog-spring-boot](https://github.com/josdem/vetlog-spring-boot) 🐶🐱

<!-- ALL-CONTRIBUTORS-BADGE:END -->

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

2. Install the dependencies

```sh
uv sync
```

3. (Optional) Verify installation

```sh
uv run check
```

## Usage

**Run**

```sh
# Filter invalid users
uv run filter_by_username

# Filter suspicious users
uv run suggest

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

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/jgafnea"><img src="https://avatars.githubusercontent.com/u/84107636?v=4?s=100" width="100px;" alt="jgafnea"/><br /><sub><b>jgafnea</b></sub></a><br /><a href="#infra-jgafnea" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a> <a href="#ideas-jgafnea" title="Ideas, Planning, & Feedback">🤔</a> <a href="#mentoring-jgafnea" title="Mentoring">🧑‍🏫</a><a href="https://github.com/josdem/py-vetlog-buddy/commits?author=jgafnea" title="Code">💻</a> </td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/kaminuma"><img src="https://avatars.githubusercontent.com/u/33448874?v=4?s=100" width="100px;" alt="T.H(kaminuma)"/><br /><sub><b>T.H(kaminuma)</b></sub></a><br /><a href="https://github.com/josdem/py-vetlog-buddy/pulls?q=is%3Apr+reviewed-by%3Akaminuma" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/blu3-bird"><img src="https://avatars.githubusercontent.com/u/194448323?v=4?s=100" width="100px;" alt="Pardeep Singh"/><br /><sub><b>Pardeep Singh</b></sub></a><br /><a href="https://github.com/josdem/py-vetlog-buddy/commits?author=blu3-bird" title="Code">💻</a> <a href="https://github.com/josdem/py-vetlog-buddy/commits?author=blu3-bird" title="Documentation">📖</a></td>
    </tr>
  </tbody>
</table>

- https://github.com/josdem/py-vetlog-analyzer/wiki
- https://github.com/josdem/py-vetlog-buddy/graphs/contributors
- https://github.com/josdem/vetlog-spring-boot
- https://pypi.org/project/py-vetlog-analyzer

---

<div align="center">
  This project follows the <a href="https://github.com/all-contributors/all-contributors">all-contributors</a> specification. Contributions of any kind welcome!
</div>
