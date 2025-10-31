# Repository Overview

This repository contains two main components:

## 1. OSI Model Blockchain Simulation

A Python-based educational simulation demonstrating data flow through the seven layers of the OSI (Open Systems Interconnection) model with blockchain integration.

### Features
- Seven-layer OSI model simulation
- Encapsulation and decapsulation of data through network layers
- Encryption and digital signatures at the Presentation Layer
- Blockchain transaction handling
- Comprehensive test suite

For detailed documentation, see [osi_blockchain_simulation/README.md](osi_blockchain_simulation/README.md)

### Quick Start
```bash
cd osi_blockchain_simulation
python3 main_simulation.py --data "Hello World"
```

## 2. Fractal Mythos Explorer (Interactive Web Application)

An interactive web-based fractal visualization platform with mythological themes.

### Features
- Interactive fractal exploration
- Mythological character narratives
- Real-time canvas animations
- Generative art based on mythological themes

View the application by opening `index.html` in a web browser.

---

## GitHub Workflow Configuration

This repository includes GitHub Actions workflow configuration to ensure proper integration with GitHub Copilot and CI/CD pipelines.

### Important Documentation
- 📄 **[COPILOT_AUTHENTICATION_FIX.md](COPILOT_AUTHENTICATION_FIX.md)** - Comprehensive guide for fixing authentication errors and branch reference issues
- ⚙️ **[.github/workflows/copilot-agent-example.yml](.github/workflows/copilot-agent-example.yml)** - Example workflow with proper authentication and branch fetching configuration

### Key Fixes Implemented
- ✅ **Authentication Configuration**: Proper setup of `COPILOT_TOKEN` and `GITHUB_TOKEN` environment variables
- ✅ **Branch Fetching**: Use of `fetch-depth: 0` to ensure all branches are available for git operations
- ✅ **Token Scopes**: Documentation of required token permissions (`repo`, `workflow`)
- ✅ **Security**: `.gitignore` configuration to prevent accidental commit of secrets

For detailed troubleshooting and setup instructions, see [COPILOT_AUTHENTICATION_FIX.md](COPILOT_AUTHENTICATION_FIX.md).

---

## Additional Documentation

- [QUICKSTART.md](QUICKSTART.md) - Quick start guide
- [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) - Deployment instructions
- [SETUP_SECRETS_GUIDE.md](SETUP_SECRETS_GUIDE.md) - Guide for setting up secrets
- [roadmap.md](roadmap.md) - Project roadmap

## License

See [LICENSE](LICENSE) file for details.  
