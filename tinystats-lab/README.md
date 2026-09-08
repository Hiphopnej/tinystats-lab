# tinystats

Tiny numeric utilities (`mean`, `median`) plus a simple CLI. This project is an example of a modern Python library using `pyproject.toml` and setuptools.

## Features
- `tinystats.mean(iterable)`
- `tinystats.median(iterable)`
- CLI: `tinystats mean ...` and `tinystats median ...`

## Requirements
- Python 3.9+

## Installation (standard)
Use this when you just want to **use** the library:

```bash
# From a source checkout
pip install .
```

## Installation for developers

Use this when you want to make changes to the library code and run tests:

```
# Option A
pip install -r requirements.txt
pip install -e .

# Option B: editable install with dev extras (flexible versions)
pip install -e ".[dev]"
```

## Quick start

**Library:**
```python
from tinystats import mean, median
print(mean([1,2,3,4]))   # 2.5
print(median([1,3]))     # 2.0
```

**CLI:**
```bash
tinystats mean 1 2 3 4
tinystats median 1 3
```

## Testing & coverage

```bash
pytest
# or with explicit coverage flags (already set in pyproject)
pytest --cov=tinystats --cov-report=term-missing
```

## Versioning & dependencies

This project follows semantic versioning.

Runtime dependencies use compatible ranges in `pyproject.toml`.

Development dependencies are pinned in `requirements.txt` for reproducible environments.

## Project layout

```
src/tinystats/       # package code
tests/               # unit tests (pytest)
examples/            # usage examples
pyproject.toml       # build configuration
requirements.txt     # pinned dev/test tools
```