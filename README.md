<p align="right">
  <strong>🇺🇸 English</strong> |
  <a href="README.ko.md">🇰🇷 한국어</a>
</p>

# Litestar Boilerplate Collection

A collection of 3 project structure boilerplates based on Litestar.

## Architecture Types

### 1. Layered + Controller-Centric Structure (`layered/`)
Traditional layered architecture with controller-centric structure
- Clear layer separation (Controller, Service, Repository, Model)
- MVC pattern based
- Simple and easy to understand structure

### 2. DDD-lite (`ddd-lite/`)
Lightweight structure applying core concepts of Domain-Driven Design
- Domain-centric modeling
- Aggregates and domain services
- Hexagonal architecture elements

### 3. Feature-based Modular (`feature-based/`)
Structure modularized by features
- Complete encapsulation by features
- Vertical slicing
- Easy transition to microservices

## Language Support

This CLI tool supports Korean and English:

```bash
# Use Korean
litestar-boilerplate --language ko list-templates

# Use English (default in English environment)
litestar-boilerplate --language en list-templates

# Short option
litestar-boilerplate -l ko create --type layered --name my-app
```

📋 **Multi-language README**:
- [`README.md`](README.md) - 🇺🇸 English (GitHub default)
- [`README.ko.md`](README.ko.md) - 🇰🇷 한국어 (Korean)

## Usage

```bash
# Install CLI tool
pip install -e .

# Create new project
litestar-boilerplate create --type layered --name my-project
litestar-boilerplate create --type ddd-lite --name my-project
litestar-boilerplate create --type feature-based --name my-project

# List templates
litestar-boilerplate list-templates

# Help
litestar-boilerplate --help
```

## Requirements

- Python 3.11+
- Litestar 2.0+
- SQLAlchemy 2.0+
- Alembic
- Pydantic V2

## Development Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# Install dependencies and dev dependencies
pip install -e ".[dev]"
```

For detailed documentation of each structure, refer to the README in the respective directory.
