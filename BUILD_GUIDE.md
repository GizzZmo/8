# Build Guide

This guide explains how to build and package the OSI Blockchain Simulation project locally.

## Prerequisites

- Python 3.9 or higher
- Git
- Basic command-line knowledge

## Quick Build

### 1. Clone the Repository

```bash
git clone https://github.com/GizzZmo/8.git
cd 8
```

### 2. Run Tests

```bash
./test_all_scenarios.sh
```

### 3. Test the Simulation

```bash
cd osi_blockchain_simulation
python main_simulation.py --help
python main_simulation.py --data "Hello World"
python main_simulation.py --blockchain --encrypt --sign
```

## Building Distribution Packages

### Using setup.py (Recommended)

```bash
# Install build dependencies
pip install build wheel

# Build source and wheel distributions
python -m build

# Output will be in dist/ directory
ls -l dist/
```

### Manual Package Creation

#### Create Python Package Archive

```bash
# Create package directory structure
mkdir -p dist/osi-blockchain-simulation
cp -r osi_blockchain_simulation dist/osi-blockchain-simulation/
cp test_all_scenarios.sh dist/osi-blockchain-simulation/
cp readme.md dist/osi-blockchain-simulation/
cp LICENSE dist/osi-blockchain-simulation/
cp QUICKSTART.md dist/osi-blockchain-simulation/

# Create version information
echo "Build Date: $(date -u)" > dist/osi-blockchain-simulation/BUILD_INFO.txt
echo "Git Commit: $(git rev-parse HEAD)" >> dist/osi-blockchain-simulation/BUILD_INFO.txt

# Create archives
cd dist
tar -czf osi-blockchain-simulation.tar.gz osi-blockchain-simulation/
zip -r osi-blockchain-simulation.zip osi-blockchain-simulation/
```

#### Create Web Assets Package

```bash
mkdir -p dist/web
cp index.html dist/web/
cp readme.md dist/web/
cp main.md dist/web/
cp osi_model.md dist/web/

cd dist
tar -czf web-assets.tar.gz web/
zip -r web-assets.zip web/
```

#### Create Documentation Package

```bash
mkdir -p dist/docs
cp readme.md dist/docs/
cp main.md dist/docs/
cp osi_model.md dist/docs/
cp osi_flow_sim.md dist/docs/
cp roadmap.md dist/docs/
cp QUICKSTART.md dist/docs/
cp DEPLOYMENT_GUIDE.md dist/docs/
cp CI_CD_DOCUMENTATION.md dist/docs/
cp BUILD_GUIDE.md dist/docs/
cp LICENSE dist/docs/

cd dist
tar -czf documentation.tar.gz docs/
zip -r documentation.zip docs/
```

## Development Build

### Setting up Development Environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements.txt

# Install package in editable mode
pip install -e .
```

### Running Tests

```bash
# Run all test scenarios
./test_all_scenarios.sh

# Run specific examples
cd osi_blockchain_simulation/examples
python simple_text_flow.py
python blockchain_flow.py
python encrypted_data_flow.py
python signed_data_flow.py
```

### Code Quality Checks

```bash
# Install linting tools
pip install flake8 pylint black

# Run flake8
flake8 osi_blockchain_simulation --max-line-length=127

# Run pylint
pylint osi_blockchain_simulation

# Format code with black
black osi_blockchain_simulation
```

## Installing from Source

### System-wide Installation

```bash
# Install from source
python setup.py install

# Or using pip
pip install .
```

### User Installation

```bash
# Install for current user only
pip install --user .
```

### Editable Installation (for development)

```bash
# Install in editable mode
pip install -e .

# Now you can use the osi-simulate command
osi-simulate --help
osi-simulate --data "Test"
```

## Build Verification

### Verify Package Installation

```bash
# Check installed package
pip list | grep osi-blockchain

# Test console script
osi-simulate --version
osi-simulate --help

# Test module import
python -c "from osi_blockchain_simulation.core.layers import ApplicationLayer; print('Import successful')"
```

### Verify Archive Contents

```bash
# List contents of tar.gz
tar -tzf dist/osi-blockchain-simulation.tar.gz

# List contents of zip
unzip -l dist/osi-blockchain-simulation.zip

# Extract and test
tar -xzf dist/osi-blockchain-simulation.tar.gz
cd osi-blockchain-simulation
./test_all_scenarios.sh
```

## Platform-Specific Instructions

### Linux/macOS

```bash
# Make test script executable
chmod +x test_all_scenarios.sh

# Run tests
./test_all_scenarios.sh

# Build package
python -m build
```

### Windows

```bash
# Run tests using Python directly
cd osi_blockchain_simulation
python main_simulation.py --data "Test"

# Build package
python -m build
```

## Troubleshooting

### Import Errors

If you get import errors:
```bash
# Ensure you're in the right directory
cd /path/to/8

# Add current directory to PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:$(pwd)"

# Or install in editable mode
pip install -e .
```

### Permission Errors (Linux/macOS)

```bash
# Make scripts executable
chmod +x test_all_scenarios.sh
chmod +x osi_blockchain_simulation/main_simulation.py
```

### Missing Dependencies

```bash
# Install all dependencies
pip install -r requirements.txt

# Or install minimal dependencies
pip install setuptools wheel build
```

### Build Directory Issues

```bash
# Clean build artifacts
rm -rf build/ dist/ *.egg-info/

# Rebuild
python -m build
```

## Advanced Build Options

### Creating Wheel Only

```bash
python -m build --wheel
```

### Creating Source Distribution Only

```bash
python -m build --sdist
```

### Building with Specific Python Version

```bash
python3.11 -m build
python3.12 -m build
```

### Creating Universal Wheel

Edit `setup.py` to add:
```python
from setuptools import setup

setup(
    # ... other options ...
    options={'bdist_wheel': {'universal': True}}
)
```

## Continuous Integration

The project includes GitHub Actions workflows that automatically:
- Build packages on every commit
- Test on multiple Python versions
- Create release artifacts
- Deploy documentation

See [CI_CD_DOCUMENTATION.md](CI_CD_DOCUMENTATION.md) for details.

## Release Process

### Creating a Release

1. Update version in `setup.py` if needed (or use git tags)
2. Commit all changes
3. Create and push a version tag:
   ```bash
   git tag -a v1.0.0 -m "Release version 1.0.0"
   git push origin v1.0.0
   ```
4. GitHub Actions will automatically:
   - Run all tests
   - Build release artifacts
   - Create GitHub Release
   - Upload distribution files

### Manual Release

```bash
# Build all packages
python -m build

# Create release archives manually
./build_release.sh v1.0.0  # If you create this script

# Upload to GitHub Releases manually
# Or use gh CLI: gh release create v1.0.0 dist/*
```

## Testing the Build

### Minimal Test

```bash
# Extract archive
tar -xzf dist/osi-blockchain-simulation.tar.gz
cd osi-blockchain-simulation

# Run basic test
cd osi_blockchain_simulation
python main_simulation.py --data "Build test successful"
```

### Complete Test

```bash
# Extract and test
tar -xzf dist/osi-blockchain-simulation.tar.gz
cd osi-blockchain-simulation

# Run full test suite
./test_all_scenarios.sh

# Test all examples
cd osi_blockchain_simulation/examples
for script in *.py; do
    echo "Testing $script..."
    python "$script"
done
```

## Clean Up

```bash
# Remove build artifacts
rm -rf build/ dist/ *.egg-info/

# Remove Python cache
find . -type d -name __pycache__ -exec rm -rf {} +
find . -type f -name "*.pyc" -delete

# Remove virtual environment
rm -rf venv/
```

## Next Steps

After building:
1. Test the built packages thoroughly
2. Review [QUICKSTART.md](QUICKSTART.md) for usage instructions
3. Read [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for deployment options
4. Check [CI_CD_DOCUMENTATION.md](CI_CD_DOCUMENTATION.md) for automation details

## Support

For build issues:
- Check this guide first
- Review GitHub Actions workflow logs
- Open an issue with build error details
- Include Python version and OS information
