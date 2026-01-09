# Contributing to sphinx-needs-tree-map

Thank you for your interest in contributing to sphinx-needs-tree-map!

## Development Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/patdhlk/sphinx-needs-tree-map.git
   cd sphinx-needs-tree-map
   ```

2. Create a virtual environment and install dependencies:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -e ".[dev,docs]"
   ```

3. Install pre-commit hooks:

   ```bash
   pip install pre-commit
   pre-commit install
   ```

## Running Tests

```bash
pytest tests/ -v
```

With coverage:

```bash
pytest tests/ -v --cov=sphinx_needs_tree_map --cov-report=html
```

## Code Style

This project uses:

- **ruff** for linting and formatting
- **mypy** for type checking

Run checks manually:

```bash
ruff check sphinx_needs_tree_map tests
ruff format sphinx_needs_tree_map tests
mypy sphinx_needs_tree_map
```

Or use pre-commit:

```bash
pre-commit run --all-files
```

## Building Documentation

```bash
cd docs
make html
# Open _build/html/index.html
```

## Submitting Changes

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Make your changes and add tests
4. Ensure all tests pass and code style checks pass
5. Commit with a clear message
6. Push to your fork and create a Pull Request

## Pull Request Guidelines

- Include tests for new functionality
- Update documentation as needed
- Follow the existing code style
- Keep commits focused and atomic
- Reference any related issues

## Reporting Issues

- Use the GitHub issue templates
- Include Sphinx and sphinx-needs versions
- Provide a minimal reproducible example when possible

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
