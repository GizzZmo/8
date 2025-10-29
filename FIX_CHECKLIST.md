# GitHub Copilot Workflow Fix Checklist

Use this checklist to verify all fixes have been properly implemented.

## Authentication Fixes

### Token Configuration
- [ ] Personal access token generated with required scopes:
  - [ ] `repo` scope enabled
  - [ ] `workflow` scope enabled
  - [ ] `read:org` scope enabled (if using organization)
- [ ] Token saved in repository secrets as `COPILOT_TOKEN`
- [ ] Token expiration date noted for future renewal
- [ ] `GITHUB_TOKEN` has appropriate permissions in workflow

### Workflow Environment Variables
- [ ] Workflow file includes `COPILOT_TOKEN` in env section:
  ```yaml
  env:
    COPILOT_TOKEN: ${{ secrets.COPILOT_TOKEN }}
  ```
- [ ] Workflow file includes `GITHUB_TOKEN` in env section:
  ```yaml
  env:
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
  ```

## Branch Reference Fixes

### Checkout Configuration
- [ ] Checkout action uses `fetch-depth: 0`:
  ```yaml
  - uses: actions/checkout@v4
    with:
      fetch-depth: 0
  ```
- [ ] Checkout action includes token:
  ```yaml
  - uses: actions/checkout@v4
    with:
      token: ${{ secrets.GITHUB_TOKEN }}
  ```

### Git Configuration
- [ ] Verified default branch name (`main` vs `master`)
- [ ] Branch references in workflow match actual branch names
- [ ] Git commands that reference branches work correctly

## Security Best Practices

### Repository Configuration
- [ ] `.gitignore` file created/updated
- [ ] `.gitignore` includes patterns for secrets:
  - [ ] `.env`
  - [ ] `*.key`
  - [ ] `secrets/`
  - [ ] `credentials.json`

### Token Management
- [ ] No tokens committed in code or workflow files
- [ ] All tokens stored as GitHub Secrets
- [ ] Token permissions limited to minimum required
- [ ] Plan for regular token rotation (every 90 days)

## Testing and Validation

### Workflow Validation
- [ ] YAML syntax validated (no parsing errors)
- [ ] Workflow triggers on correct events:
  - [ ] `workflow_dispatch` (manual trigger)
  - [ ] `pull_request` (PR events)
- [ ] Workflow runs without errors

### Authentication Testing
- [ ] Workflow runs without 401 Unauthorized errors
- [ ] Copilot API calls succeed
- [ ] Session logging works (if applicable)

### Branch Access Testing
- [ ] `git branch -a` shows all branches
- [ ] `git rev-parse origin/main` succeeds
- [ ] `git diff origin/main HEAD` works without errors

## Documentation

### Files Created/Updated
- [ ] Example workflow file created: `.github/workflows/copilot-agent-example.yml`
- [ ] Authentication fix guide created: `COPILOT_AUTHENTICATION_FIX.md`
- [ ] Quick setup guide created: `SETUP_SECRETS_GUIDE.md`
- [ ] README updated with workflow documentation
- [ ] `.gitignore` created/updated

### Documentation Quality
- [ ] All documentation is clear and accurate
- [ ] Examples include actual repository names/paths
- [ ] Troubleshooting sections are comprehensive
- [ ] Links between documents work correctly

## Post-Implementation

### Monitoring
- [ ] Workflow runs monitored for first week
- [ ] Authentication errors logged and resolved
- [ ] Branch access issues logged and resolved

### Maintenance Plan
- [ ] Token expiration date added to calendar
- [ ] Process for token renewal documented
- [ ] Team members notified of new workflow configuration
- [ ] Repository contributors have access to documentation

## Success Criteria

All items below must be true for complete success:

✅ **No Authentication Errors**
- Workflow runs complete without 401 errors
- All Copilot API calls succeed
- Logs show successful authentication

✅ **Branch Access Works**
- All branches are accessible in workflows
- Git commands referencing `main` work correctly
- No "unknown revision or path" errors

✅ **Security Maintained**
- No secrets committed to repository
- All tokens stored in GitHub Secrets
- `.gitignore` prevents accidental commits

✅ **Documentation Complete**
- Comprehensive guides available
- Team members can follow setup process
- Troubleshooting resources accessible

## Final Verification

Run these commands to verify all fixes:

```bash
# 1. Verify workflow YAML syntax
yamllint .github/workflows/*.yml

# 2. Check for accidentally committed secrets
git grep -i "token\|secret\|password\|api.key" | grep -v "secrets\."

# 3. Verify .gitignore patterns
git check-ignore -v .env secrets/ *.key

# 4. Test git branch access
git fetch --all
git branch -a
git rev-parse origin/main

# 5. Verify GitHub secrets configured
# (Manual check in repository Settings → Secrets)
```

## Status

- **Date Implemented**: _________________
- **Implemented By**: _________________
- **Verified By**: _________________
- **Status**: [ ] Complete [ ] In Progress [ ] Pending

## Notes

_Use this space for any additional notes or observations:_

---

**Last Updated**: 2025-10-29
**Version**: 1.0
