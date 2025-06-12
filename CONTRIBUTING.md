# Contributing to Litestar Boilerplate Collection

Thank you for your interest in contributing to the Litestar Boilerplate Collection! This document provides guidelines and information for contributors.

## 🤝 How to Contribute

### Reporting Issues
- Use the GitHub issue tracker to report bugs or request features
- Search existing issues before creating a new one
- Provide detailed information including:
  - Steps to reproduce the issue
  - Expected vs actual behavior
  - Environment details (Python version, OS, etc.)
  - Relevant code snippets or error messages

### Submitting Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Install development dependencies**:
   ```bash
   pip install -e ".[dev]"
   ```
3. **Make your changes** following our coding standards
4. **Add tests** for new functionality
5. **Run the test suite**:
   ```bash
   pytest tests/ -v
   ```
6. **Run linting and formatting**:
   ```bash
   ruff check .
   ruff format .
   mypy src/
   ```
7. **Update documentation** if needed
8. **Submit a pull request** with a clear description

## 🏗️ Development Setup

### Prerequisites
- Python 3.11 or higher
- Git

### Setup Steps
```bash
# Clone your fork
git clone https://github.com/your-username/litestar-boilerplate.git
cd litestar-boilerplate

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# Install in development mode
pip install -e ".[dev]"

# Verify installation
litestar-boilerplate --version
```

## 📝 Coding Standards

### Python Code Style
- Follow PEP 8 guidelines
- Use Ruff for linting and formatting
- Add type hints to all functions and classes
- Write docstrings for all public functions and classes (PEP 257)
- Maximum line length: 120 characters

### Code Quality
- Write tests for new functionality
- Maintain test coverage above 80%
- Use meaningful variable and function names
- Keep functions small and focused
- Add comments for complex logic

### Architecture Guidelines
- Follow the existing project structure
- Keep generators modular and extensible
- Maintain separation of concerns
- Use dependency injection where appropriate

## 🧪 Testing

### Running Tests
```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ -v --cov=src/litestar_boilerplate --cov-report=html

# Run specific test file
pytest tests/test_cli.py -v
```

### Writing Tests
- Place tests in the `tests/` directory
- Use descriptive test names
- Test both success and failure cases
- Mock external dependencies
- Use pytest fixtures for common setup

## 🌍 Internationalization (i18n)

### Adding New Messages
1. Add messages to both `MESSAGES_KO` and `MESSAGES_EN` in `src/litestar_boilerplate/i18n.py`
2. Use the `t()` function to access messages in code
3. Test with both languages:
   ```bash
   litestar-boilerplate -l ko list-templates
   litestar-boilerplate -l en list-templates
   ```

### Translation Guidelines
- Keep messages concise but informative
- Use consistent terminology
- Consider cultural context for Korean translations
- Test CLI output in both languages

## 🏛️ Architecture Contributions

### Adding New Architecture Templates
1. Create a new generator class in `src/litestar_boilerplate/generators/`
2. Implement the `ArchitectureGenerator` interface
3. Add template information to i18n messages
4. Update the factory in `generator_factory.py`
5. Add comprehensive tests
6. Update documentation

### Template Structure Guidelines
- Include complete project setup (pyproject.toml, .env.example, etc.)
- Provide working CRUD examples
- Include authentication and security features
- Add comprehensive tests
- Follow Python best practices
- Include detailed README for the template

## 📚 Documentation

### README Updates
- Use the built-in README generator: `litestar-boilerplate generate-readme`
- Update i18n messages for new content
- Maintain consistency between Korean and English versions

### Code Documentation
- Write clear docstrings for all public APIs
- Include usage examples in docstrings
- Keep inline comments up to date
- Document complex algorithms or business logic

## 🚀 Release Process

### Version Numbering
- Follow Semantic Versioning (SemVer)
- Update version in `pyproject.toml`
- Create release notes highlighting changes

### Release Checklist
- [ ] All tests pass
- [ ] Documentation is updated
- [ ] Version number is bumped
- [ ] CHANGELOG is updated
- [ ] Release notes are prepared

## 🏷️ Issue Labels

Use these labels when creating issues:

- `bug` - Something isn't working
- `enhancement` - New feature or request
- `documentation` - Improvements to documentation
- `good first issue` - Good for newcomers
- `help wanted` - Extra attention needed
- `architecture:layered` - Related to layered architecture
- `architecture:ddd-lite` - Related to DDD-lite architecture
- `architecture:feature-based` - Related to feature-based architecture
- `i18n` - Internationalization related
- `cli` - CLI tool related

## 💬 Community

- Be respectful and inclusive
- Help others learn and grow
- Share knowledge and best practices
- Provide constructive feedback

## 📄 License

By contributing to this project, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to the Litestar Boilerplate Collection! 🎉 