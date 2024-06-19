Python Vetlog Analyzer
----------------------------

Data analysis for [Vetlog](https://vetlog.org/) database

#### Requirements

- Python version `3.11.9` or above

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