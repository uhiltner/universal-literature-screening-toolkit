# Contributing to Universal Literature Screening Toolkit

Thank you for your interest in contributing to the Universal Literature Screening Toolkit! This document provides guidelines for contributing to the project.

## How to Contribute

### Reporting Bugs

If you find a bug, please create an issue on GitHub with:

- **Clear description** of the problem
- **Steps to reproduce** the issue
- **Expected vs. actual behavior**
- **System information** (OS, Python version)
- **Sample files** (if applicable and not confidential)

### Suggesting Features

I welcome feature suggestions! Please create an issue with:

- **Clear description** of the proposed feature
- **Use case** explaining why this feature would be valuable
- **Possible implementation** ideas (if you have any)

### Contributing Code

1. **Fork the repository** and create a new branch for your feature or bug fix
2. **Write tests** for any new functionality
3. **Ensure all tests pass** by running `python -m pytest tests/`
4. **Follow coding standards** (see below)
5. **Update documentation** if necessary
6. **Submit a pull request** with a clear description of your changes

## Development Setup

1. Clone your fork of the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Install development dependencies: `pip install pytest pytest-cov`

## Coding Standards

- **Follow PEP 8** Python style guidelines
- **Use descriptive variable and function names**
- **Add docstrings** to all functions and classes
- **Include type hints** where appropriate
- **Keep functions focused** and reasonably sized
- **Comment complex logic** clearly

## Testing

- **Write tests** for new functionality using pytest
- **Maintain test coverage** above 80%
- **Test edge cases** and error conditions
- **Include integration tests** for complex workflows

Run tests with:
```bash
python -m pytest tests/ -v
```

## Documentation

- **Update README.md** if adding new features
- **Update user_manual.md** for user-facing changes
- **Include docstrings** in code
- **Provide examples** for new functionality

## Domain-Specific Contributions

I especially welcome contributions that:

- **Add new language support** (search patterns for additional languages)
- **Provide domain templates** for new research fields
- **Improve PDF extraction** for challenging document formats
- **Enhance validation logic** with new operators or criteria types

## Questions?

If you have questions about contributing, please:

1. Check existing issues and discussions
2. Create a new issue with the "question" label
3. Contact the maintainer: ulrike.hiltner@usys.ethz.ch

## Recognition

Contributors will be acknowledged in:
- The CONTRIBUTORS.md file
- Release notes for significant contributions
- Academic publications when appropriate

Thank you for helping make systematic literature review more accessible to researchers worldwide!
