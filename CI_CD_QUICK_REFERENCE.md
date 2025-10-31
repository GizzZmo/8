# CI/CD Quick Reference

## Workflow Triggers

| Workflow | Automatic Triggers | Manual Trigger |
|----------|-------------------|----------------|
| **CI Build** | Push/PR to main/develop | ✅ Yes |
| **Release** | Push tags `v*` | ✅ Yes (with version input) |
| **GitHub Pages** | Push to main (HTML/MD changes) | ✅ Yes |
| **Nightly** | Daily at 2 AM UTC | ✅ Yes |

## Quick Actions

### Run CI Manually
```bash
# Via GitHub UI: Actions → CI - Build and Test → Run workflow
```

### Create a Release
```bash
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0
# Release workflow runs automatically
```

### Trigger Manual Release
```bash
# Via GitHub UI: Actions → Release - Create Artifacts → Run workflow
# Enter version: v1.0.0
```

### Deploy to GitHub Pages
```bash
# Automatic on push to main with HTML/MD changes
# Or via GitHub UI: Actions → Deploy - GitHub Pages → Run workflow
```

## Artifacts

### Download from Actions
1. Go to Actions tab
2. Click on a workflow run
3. Scroll to Artifacts section
4. Download desired artifact

### Artifact Types
- **python-package**: Complete Python simulation
- **web-assets**: Web interface files
- **documentation**: All docs in archive format
- **release-{version}**: Complete release bundle
- **nightly-build-{date}**: Daily build snapshot

## CI Status

### Check Status Badges
Visit the [README](readme.md) to see current status:
- CI Build Status
- GitHub Pages Deploy Status
- Nightly Build Status

### View Workflow Logs
1. Actions tab → Select workflow
2. Click on a run → Select job
3. View logs or download

## Common Tasks

### Test Locally Before Push
```bash
./test_all_scenarios.sh
```

### Build Package Locally
```bash
python -m build
```

### Verify Workflow YAML
```bash
# Install yamllint
pip install yamllint

# Check workflows
yamllint .github/workflows/*.yml
```

### Clean Build Artifacts
```bash
rm -rf build/ dist/ *.egg-info/ __pycache__/
```

## Workflow Files

| File | Purpose |
|------|---------|
| `ci.yml` | Main CI/CD pipeline |
| `release.yml` | Release management |
| `deploy-pages.yml` | GitHub Pages deployment |
| `nightly.yml` | Nightly comprehensive tests |

## Retention Policies

| Artifact Type | Retention Period |
|--------------|------------------|
| CI Builds | 30 days |
| Releases | 90 days |
| Documentation | 90 days |
| Nightly Builds | 7 days |

## Python Versions Tested

- Python 3.9
- Python 3.10
- Python 3.11
- Python 3.12

## Platforms Tested (Nightly)

- Ubuntu Latest
- Windows Latest
- macOS Latest

## Troubleshooting

### Workflow Failed
1. Check logs in Actions tab
2. Look for red ❌ indicators
3. Click job name to see details
4. Fix issue and push again

### Artifact Not Created
1. Verify workflow completed successfully
2. Check artifact upload step in logs
3. Ensure artifact path exists
4. Check retention period hasn't expired

### Page Deploy Failed
1. Verify GitHub Pages is enabled
2. Check repository settings → Pages
3. Ensure workflow has correct permissions
4. Review deploy job logs

## Documentation

- [CI_CD_DOCUMENTATION.md](CI_CD_DOCUMENTATION.md) - Complete CI/CD guide
- [BUILD_GUIDE.md](BUILD_GUIDE.md) - Local build instructions
- [QUICKSTART.md](QUICKSTART.md) - Quick start guide
- [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) - Deployment instructions

## Support

- GitHub Issues: Tag with `ci/cd` label
- Check workflow logs first
- Include error messages in bug reports
- Mention OS and Python version

## Best Practices

1. ✅ Test locally before pushing
2. ✅ Use meaningful commit messages
3. ✅ Tag releases with semantic versioning
4. ✅ Check CI status before merging PRs
5. ✅ Review workflow logs regularly
6. ✅ Keep dependencies updated
7. ✅ Clean up old artifacts periodically

## Environment Variables

| Variable | Used In | Purpose |
|----------|---------|---------|
| `GITHUB_TOKEN` | All workflows | GitHub API authentication |
| `COPILOT_TOKEN` | Example workflow | Copilot agent authentication |

## Permissions Required

| Workflow | Permissions |
|----------|------------|
| CI Build | `contents: read` |
| Release | `contents: write` |
| GitHub Pages | `contents: read`, `pages: write`, `id-token: write` |
| Nightly | `contents: read` |

## Quick Links

- [Actions Tab](../../actions)
- [Releases](../../releases)
- [GitHub Pages](../../pages)
- [Settings](../../settings)

---

**Last Updated:** 2025-10-31  
**Version:** 1.0.0
