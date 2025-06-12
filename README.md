<p align="right">
  <strong>🇺🇸 English</strong> |
  <a href="README.ko.md">🇰🇷 한국어</a>
</p>

# Litestar Boilerplate Collection

🚀 Production-ready boilerplates for modern and scalable Python web applications

[![CI/CD Pipeline](https://github.com/your-username/litestar-boilerplate/workflows/CI%2FCD%20Pipeline/badge.svg)](https://github.com/your-username/litestar-boilerplate/actions)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Litestar](https://img.shields.io/badge/Litestar-2.0+-green.svg)](https://litestar.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)

A collection of 3 Litestar-based project structure boilerplates.

## ✨ Key Features

- 🏗️ **3 Architecture Patterns**: Support for Layered, DDD-lite, and Feature-based structures
- 🌍 **Multilingual CLI**: Korean/English support for global development teams
- ⚡ **Ready to Use**: Complete CRUD, authentication, and testing structure included
- 🔧 **Modern Stack**: Based on Litestar 2.0, SQLAlchemy 2.0, Pydantic V2
- 📚 **Rich Documentation**: Detailed guides for each architecture
- 🧪 **Test-First**: Complete testing environment with pytest

## 🏛️ Architecture Types

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

## 🚀 Usage

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

## 🌍 Language Support

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

## 📋 Requirements

- Python 3.11+
- Litestar 2.0+
- SQLAlchemy 2.0+
- Alembic
- Pydantic V2

## 🛠️ Development Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# Install dependencies and dev dependencies
pip install -e ".[dev]"
```

## 🧩 Litestar Resources

### 📖 Official Documentation & Repositories
- [**Litestar Official Docs**](https://docs.litestar.dev/) - Complete API documentation and guides
- [**Litestar GitHub**](https://github.com/litestar-org/litestar) - Main repository
- [**Litestar Fullstack Example**](https://github.com/litestar-org/litestar-fullstack) - Real production example

### 🎓 Learning Resources
- [**Awesome Litestar**](https://github.com/litestar-org/awesome-litestar) - Curated collection of Litestar resources
- [**Litestar Tutorials**](https://docs.litestar.dev/latest/tutorials/) - Step-by-step learning guides
- [**Litestar Examples**](https://github.com/litestar-org/litestar/tree/main/docs/examples) - Various use case examples

### 🛠️ Tools & Plugins
- [**Litestar CLI**](https://docs.litestar.dev/latest/usage/cli/) - Powerful command-line tool
- [**Advanced Alchemy**](https://github.com/litestar-org/advanced-alchemy) - SQLAlchemy extensions
- [**Litestar Users**](https://github.com/litestar-org/litestar-users) - User management plugin

## 📚 Detailed Documentation

For detailed documentation and examples of each structure, refer to the README in the respective directory.

## 🤝 Contributing

If you'd like to contribute to this project, please create an issue or submit a pull request. All contributions are welcome!

## 📄 License

This project is distributed under the MIT License.
