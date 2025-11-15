Python Vetlog Analyzer

<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-3-orange.svg?style=flat-square)](#contributors-)
[![GitHub](https://github.com/josdem/py-vetlog-analyzer/actions/workflows/main.yml/badge.svg)](https://github.com/josdem/py-vetlog-analyzer/actions)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=josdem_py-vetlog-analyzer&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=josdem_py-vetlog-analyzer)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

Data analysis for [Vetlog](https://vetlog.org/) database

#### Requirements

- Python version `3.12.3` or above

#### To install dependencies

```bash
poetry install
```

#### To format code

```bash
python -m black "py_vetlog_analyzer" "tests"
```

#### To run tests

```bash
python -m unittest discover -s tests
```

#### To run a single test

```bash
python -m unittest tests/${test_name}.py
```

Where:
- `${test_name}.py` is the test name you want to run

#### To run with poetry

```bash
poetry run filterByUsername
poetry run filterByName
poetry run suspicious
poetry run vaccines
```

**Where:**

- `filter` Filters invalid users from the database
- `suspicious` Filters suspicious users (Maybe invalid users) from the database
- `vaccines` Generates expected vaccination records for pets without pending vaccination plan

#### To run coverage

```bash
coverage run -m unittest discover
coverage report -m
coverage html
```

#### Configuration

https://github.com/josdem/py-vetlog-analyzer/wiki

#### PyPi project

https://pypi.org/project/py-vetlog-analyzer/

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/jgafnea"><img src="https://avatars.githubusercontent.com/u/84107636?v=4?s=100" width="100px;" alt="jgafnea"/><br /><sub><b>jgafnea</b></sub></a><br /><a href="#infra-jgafnea" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a> <a href="#ideas-jgafnea" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/kaminuma"><img src="https://avatars.githubusercontent.com/u/33448874?v=4?s=100" width="100px;" alt="T.H(kaminuma)"/><br /><sub><b>T.H(kaminuma)</b></sub></a><br /><a href="https://github.com/josdem/py-vetlog-analyzer/pulls?q=is%3Apr+reviewed-by%3Akaminuma" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/blu3-bird"><img src="https://avatars.githubusercontent.com/u/194448323?v=4?s=100" width="100px;" alt="Pardeep Singh"/><br /><sub><b>Pardeep Singh</b></sub></a><br /><a href="https://github.com/josdem/py-vetlog-analyzer/commits?author=blu3-bird" title="Code">💻</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
