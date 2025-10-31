# CI/CD System Documentation

## Overview

This repository includes a comprehensive CI/CD (Continuous Integration/Continuous Deployment) system that automatically builds, tests, and packages artifacts for the OSI Blockchain Simulation project.

## Workflows

### 1. CI - Build and Test (`.github/workflows/ci.yml`)

**Triggers:**
- Push to `main` or `develop` branches
- Pull requests to `main` or `develop` branches
- Manual workflow dispatch

**Jobs:**

#### Test Job
- Runs on multiple Python versions (3.9, 3.10, 3.11, 3.12)
- Executes all test scenarios
- Tests main simulation with various configurations
- Tests all example flows

#### Lint Job
- Runs flake8 for code quality checks
- Runs pylint for additional code analysis
- Continues on error to not block builds

#### Build Artifacts Job
- Creates distributable Python package
- Generates build information (date, commit, branch)
- Creates TAR.GZ and ZIP archives
- Uploads artifacts with 30-day retention

#### Build Web Assets Job
- Packages web interface (index.html)
- Includes documentation files
- Creates web asset archives
- Uploads artifacts with 30-day retention

#### Build Docs Job
- Packages all documentation
- Creates comprehensive documentation archives
- Uploads with 90-day retention

### 2. Release - Create Artifacts (`.github/workflows/release.yml`)

**Triggers:**
- Push to tags matching `v*` pattern
- Manual workflow dispatch with version input

**Features:**
- Automated version detection from git tags
- Runs full test suite before release
- Creates versioned release packages:
  - Python package with all source code
  - Web assets bundle
  - Complete documentation package
- Generates detailed release notes
- Uploads all artifacts to GitHub Releases
- 90-day artifact retention

**Release Packages Include:**
- Python simulation code
- Test scripts
- Documentation
- License information
- Release metadata

### 3. Deploy - GitHub Pages (`.github/workflows/deploy-pages.yml`)

**Triggers:**
- Push to `main` branch affecting:
  - `index.html`
  - Any markdown files
- Manual workflow dispatch

**Features:**
- Automatic deployment to GitHub Pages
- Serves web interface and documentation
- Creates user-friendly documentation site
- Automatic URL generation

**Deployed Content:**
- Interactive web interface
- All documentation files
- Quick start guide
- OSI model reference

### 4. Nightly - Build and Test (`.github/workflows/nightly.yml`)

**Triggers:**
- Daily at 2 AM UTC
- Manual workflow dispatch

**Features:**
- Cross-platform testing (Ubuntu, Windows, macOS)
- Tests on all supported Python versions
- Comprehensive test coverage including:
  - Basic functionality
  - Edge cases
  - Unicode support
  - Combined feature testing
- Creates nightly build packages
- 7-day artifact retention

## Artifacts

The CI system produces several types of artifacts:

### Python Package
- **Contents:** Complete OSI simulation implementation
- **Format:** `.tar.gz` and `.zip`
- **Includes:**
  - All Python modules
  - Test scripts
  - Documentation
  - License

### Web Assets
- **Contents:** Web interface and documentation
- **Format:** `.tar.gz` and `.zip`
- **Includes:**
  - `index.html`
  - Markdown documentation
  - Quick start guides

### Documentation
- **Contents:** Comprehensive project documentation
- **Format:** `.tar.gz` and `.zip`
- **Includes:**
  - All markdown files
  - Guides and tutorials
  - Implementation notes
  - License information

## Using the Artifacts

### Downloading from GitHub Actions

1. Navigate to the Actions tab in the repository
2. Select the workflow run you're interested in
3. Scroll to the "Artifacts" section at the bottom
4. Download the desired artifact

### Using Release Artifacts

1. Go to the Releases page
2. Find the desired version
3. Download the appropriate archive
4. Extract and follow the included documentation

### Installation from Package

```bash
# Download and extract the Python package
tar -xzf osi-blockchain-simulation-v1.0.0.tar.gz
cd osi-blockchain-simulation-v1.0.0

# Run tests
./test_all_scenarios.sh

# Run simulation
cd osi_blockchain_simulation
python main_simulation.py --help
```

## Local Development

### Installing Development Dependencies

```bash
pip install -r requirements.txt
```

### Running Tests Locally

```bash
./test_all_scenarios.sh
```

### Building Locally

```bash
# Build Python package
python setup.py sdist bdist_wheel

# Create distribution archives
mkdir -p dist/package
cp -r osi_blockchain_simulation dist/package/
tar -czf dist/osi-blockchain-simulation.tar.gz -C dist package/
```

## CI/CD Best Practices

### Workflow Triggers
- Use `push` for main branches to catch issues early
- Use `pull_request` to validate changes before merge
- Use `workflow_dispatch` for manual testing and releases
- Use `schedule` for regular comprehensive testing

### Artifact Management
- Short retention (7 days) for frequent builds (nightly)
- Medium retention (30 days) for development artifacts
- Long retention (90 days) for releases and documentation

### Testing Strategy
- Test on multiple Python versions for compatibility
- Test on multiple platforms for portability
- Run comprehensive tests nightly to catch regressions
- Run quick tests on every commit for fast feedback

## Monitoring

### Workflow Status
Check the status badges in the README:
- [![CI - Build and Test](https://github.com/GizzZmo/8/actions/workflows/ci.yml/badge.svg)](https://github.com/GizzZmo/8/actions/workflows/ci.yml)
- [![Deploy - GitHub Pages](https://github.com/GizzZmo/8/actions/workflows/deploy-pages.yml/badge.svg)](https://github.com/GizzZmo/8/actions/workflows/deploy-pages.yml)
- [![Nightly - Build and Test](https://github.com/GizzZmo/8/actions/workflows/nightly.yml/badge.svg)](https://github.com/GizzZmo/8/actions/workflows/nightly.yml)

### Viewing Logs
1. Go to the Actions tab
2. Select the workflow run
3. Click on a job to see detailed logs
4. Download logs for offline analysis if needed

## Troubleshooting

### Failed Builds
1. Check the workflow logs for error messages
2. Verify Python version compatibility
3. Ensure all dependencies are available
4. Test locally using the same Python version

### Failed Deployments
1. Verify GitHub Pages is enabled in repository settings
2. Check workflow permissions
3. Ensure GITHUB_TOKEN has appropriate scopes

### Artifact Upload Issues
1. Verify artifact paths are correct
2. Check artifact size limits
3. Ensure retention days are within allowed range

## Future Enhancements

Potential improvements to the CI/CD system:
- Code coverage reporting
- Performance benchmarking
- Security scanning integration
- Automated dependency updates
- Docker container builds
- PyPI package publishing
- Automated changelog generation

## Security Considerations

- Secrets are managed through GitHub Secrets
- Tokens have minimal required permissions
- Dependencies are pinned for reproducibility
- Code quality checks prevent obvious vulnerabilities
- Build artifacts are scanned for sensitive data

## Support

For issues with the CI/CD system:
1. Check the workflow logs
2. Review this documentation
3. Open an issue on GitHub
4. Tag with `ci/cd` label
