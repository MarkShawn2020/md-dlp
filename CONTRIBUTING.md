# Contributing to md-dlp

Thank you for your interest in contributing to md-dlp! This document provides guidelines and best practices for contributing to this project.

## Development Setup

1. Clone the repository:
```bash
git clone https://github.com/markshawn2020/md-dlp.git
cd md-dlp
```

2. Install development dependencies:
```bash
pip install -e .
```

## Code Style

- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and single-purpose
- Maximum file length: 200 lines

## Version Management

1. Version number is maintained in `md_dlp/__init__.py`
2. Follow semantic versioning:
   - MAJOR version for incompatible API changes
   - MINOR version for added functionality in a backward compatible manner
   - PATCH version for backward compatible bug fixes

## Making Changes

1. Create a new branch for your feature/fix:
```bash
git checkout -b feature/your-feature-name
```

2. Make your changes
3. Update tests if necessary
4. Update documentation if necessary
5. Commit your changes using conventional commit format:
```bash
git commit -m "feat: add new feature"
git commit -m "fix: resolve issue with..."
```

## Release Process

1. Update version in `md_dlp/__init__.py`
2. Commit changes
3. Create and push a new tag:
```bash
git tag v0.x.x
git push origin v0.x.x
```

4. GitHub Actions will automatically:
   - Build the package
   - Publish to PyPI
   - Create a GitHub release

## Pull Request Process

1. Ensure your code follows the style guidelines
2. Update the README.md if necessary
3. The PR will be merged once you have the sign-off of a maintainer

## Questions?

Feel free to open an issue if you have any questions or need clarification.
