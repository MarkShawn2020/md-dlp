# md-dlp

A tool for markdown data loss prevention.

## Installation

### Using pip (Recommended)

```bash
pip install md-dlp
```

### Using Homebrew (Coming Soon)

> ⚠️ Homebrew installation is currently under development and not yet available. Please use pip installation for now.

The following will be available once the Homebrew formula is ready:
```bash
# Add the tap
brew tap markshawn2020/tools

# Install md-dlp
brew install md-dlp
```

## Usage

```bash
# Show help
md-dlp -h

# Show version
md-dlp -v

# Download content and save to current directory
md-dlp <URL>

# Download content and save to specific directory
md-dlp -o <output_dir> <URL>
```

## Project Structure

```
md-dlp/
├── md_dlp/
│   ├── __init__.py  # Package metadata and version
│   └── main.py      # Core functionality
├── setup.py         # Package configuration
└── README.md       # This file
```

## Development

### Version Management
- Version number is maintained in `md_dlp/__init__.py`
- Follow semantic versioning (MAJOR.MINOR.PATCH)
- Version is automatically synchronized across the package

### Best Practices
1. Single Source of Truth
   - Version number is kept in `__init__.py`
   - Setup.py reads version from `__init__.py`
   - CLI version display reads from the same source

2. Command Line Interface
   - Uses argparse for robust argument parsing
   - Supports both positional and optional arguments
   - Version flag (-v/--version) works without requiring URL

3. Code Organization
   - Follows Python package structure best practices
   - Separates package metadata from core functionality
   - Uses dependency injection for better maintainability

## Features

- Prevent data loss in markdown files
- Easy to use command-line interface
- Cross-platform support
- Available through pip (Homebrew coming soon)
- Standardized version management
- Clean and maintainable code structure

## License

MIT License

## Author

MarkShawn (shawninjuly@gmail.com)
