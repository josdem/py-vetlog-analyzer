Python Vetlog Analyzer
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
----------------------------

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

or

```bash
python3 -m unittest discover -s tests
```

#### To run with poetry
```bash
poetry run filter
poetry run suspicious
```

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
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!