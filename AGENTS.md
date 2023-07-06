# AGENTS.md

## Project Overview

`pyutils` is a Python utility library providing common helper functions and validators for personal use across projects.

## Project Structure

- `pyutils/dicts/` - Dictionary utilities (cleaning, copying, key transformations)
- `pyutils/lists/` - List utilities (flattening)
- `pyutils/paths/` - Path utilities (temporary directory management)
- `pyutils/shortcuts/` - Boolean checks and date utilities
- `pyutils/strings/` - String manipulation, cleaning, and transformations
- `pyutils/validators/` - Validation functions (email, URL, IBAN, BIC, DNI, ISIN, FIGI)

## Development Setup

```bash
# Install dependencies
pip install -r requirements-dev.txt

# Run tests
pytest

# Type checking
mypy pyutils

# Pre-commit hooks
pre-commit run
```

## Tooling

- **Type checking**: MyPy (strict mode) and Pyright
- **Linting/formatting**: Ruff
- **Testing**: pytest with coverage
- **Pre-commit**: configured in `.pre-commit-config.yaml`

## Code Style Guidelines

- Strict type hints required (no `Any`, `Optional` without explicit `None`)
- No untyped definitions or incomplete type hints
- Generic types must be fully parameterized
- List, dict, and set inference is strict

## Working with the Codebase

1. Add new utilities to the appropriate module under `pyutils/`
2. Include type hints for all function signatures
3. Write tests in the corresponding `tests/` directory
4. Run `mypy pyutils` to ensure type safety
5. Run `pytest` to verify functionality
6. Commit with conventional commit messages
