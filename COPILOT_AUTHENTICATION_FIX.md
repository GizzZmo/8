# GitHub Copilot Authentication and Branch Reference Fixes

## Problem Summary

This document addresses two critical issues encountered when running GitHub Copilot workflows:

1. **401 Unauthorized Authentication Errors** when accessing the GitHub Copilot API
2. **"fatal: ambiguous argument 'refs/heads/main': unknown revision or path not in the working tree"** error

---

## Issue 1: Authentication Errors (401 Unauthorized)

### Symptoms

Workflow logs show errors like:
```
401 Unauthorized: unauthorized: AuthenticateToken authentication failed
Request to agent callback at https://api.githubcopilot.com/agents/swe/agent/jobs failed with status 401
Failed to list models: 401 Unauthorized: unauthorized: unauthorized: AuthenticateToken authentication failed
```

### Root Causes

1. **Missing or Invalid Token**: The `COPILOT_TOKEN` or `GITHUB_TOKEN` used for authentication is:
   - Not configured as a repository secret
   - Expired or revoked
   - Missing required scopes

2. **Incorrect Token Scopes**: The token doesn't have the necessary permissions to access Copilot APIs

### Solutions

#### Step 1: Verify and Update Secrets

1. Navigate to your repository on GitHub
2. Go to **Settings** → **Secrets and variables** → **Actions**
3. Check if `COPILOT_TOKEN` exists:
   - If missing, add it with a valid GitHub token
   - If present, verify it hasn't expired
4. Ensure `GITHUB_TOKEN` has appropriate permissions

#### Step 2: Configure Required Token Scopes

For Copilot agent integration, your token must have these scopes:
- ✅ `repo` - Full control of private repositories
- ✅ `workflow` - Update GitHub Action workflows
- ✅ `read:org` (if applicable) - Read organization membership

To create or update a token with proper scopes:
1. Go to **Settings** → **Developer settings** → **Personal access tokens** → **Tokens (classic)**
2. Click "Generate new token (classic)"
3. Select the required scopes listed above
4. Copy the token and add it to repository secrets

#### Step 3: Update Workflow Configuration

Ensure your workflow file includes proper environment variables:

```yaml
env:
  COPILOT_TOKEN: ${{ secrets.COPILOT_TOKEN }}
  GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

jobs:
  your-job:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
```

---

## Issue 2: Missing Main Branch Reference

### Symptoms

Workflow logs show:
```
fatal: ambiguous argument 'refs/heads/main': unknown revision or path not in the working tree.
Use '--' to separate paths from revisions
```

This error occurs when the workflow tries to compare branches but `main` is not available locally.

### Root Cause

The default checkout action (`actions/checkout@v4`) only fetches:
- The current branch
- Shallow history (1 commit deep)

This means other branches like `main` are not available for git operations.

### Solution

Update your checkout step to fetch all branches and history:

```yaml
- name: Checkout code
  uses: actions/checkout@v4
  with:
    fetch-depth: 0  # CRITICAL: Fetch all branches and history
    token: ${{ secrets.GITHUB_TOKEN }}
```

#### What this does:
- `fetch-depth: 0` fetches **complete history** and **all branches**
- Ensures `refs/heads/main` is available for git commands
- Allows branch comparisons, diffs, and merges to work correctly

---

## Complete Example Workflow

See `.github/workflows/copilot-agent-example.yml` for a complete working example that addresses both issues.

Key elements:
```yaml
env:
  COPILOT_TOKEN: ${{ secrets.COPILOT_TOKEN }}
  GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

jobs:
  copilot-agent:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
        with:
          fetch-depth: 0  # Fetch all branches
          token: ${{ secrets.GITHUB_TOKEN }}
      
      - name: Verify main branch
        run: |
          git branch -a
          git rev-parse origin/main
```

---

## Testing the Fixes

After implementing these changes:

1. **Verify Secrets**: Ensure tokens are set in repository settings
2. **Test Locally**: Clone with all history: `git clone --depth=0 <repo-url>`
3. **Trigger Workflow**: Run the workflow manually or via pull request
4. **Check Logs**: Verify no 401 errors and `main` branch is accessible

---

## Troubleshooting

### Still Getting 401 Errors?

1. **Regenerate Token**: Create a new personal access token with correct scopes
2. **Check Organization Settings**: Ensure Copilot is enabled for your organization
3. **Verify Secret Name**: Ensure the secret name matches exactly (case-sensitive)
4. **Token Expiration**: Check if the token has an expiration date

### Main Branch Still Not Found?

1. **Verify Branch Name**: Some repositories use `master` instead of `main`
2. **Update References**: Change `refs/heads/main` to `refs/heads/master` if needed
3. **Check Default Branch**: Go to repository Settings → Branches to see the default branch

---

## Security Best Practices

1. **Never commit tokens** in code or workflow files
2. **Use secrets** for all sensitive values
3. **Limit token scopes** to only what's required
4. **Rotate tokens regularly** and revoke unused ones
5. **Enable branch protection** for main/master branches

---

## Additional Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Configuring GitHub Tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
- [Checkout Action Documentation](https://github.com/actions/checkout)
- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)

---

## Summary

**For Authentication Issues:**
- ✅ Add/update `COPILOT_TOKEN` in repository secrets
- ✅ Ensure token has `repo` and `workflow` scopes
- ✅ Reference token in workflow: `${{ secrets.COPILOT_TOKEN }}`

**For Branch Reference Issues:**
- ✅ Use `fetch-depth: 0` in checkout action
- ✅ Verify default branch name (main vs master)
- ✅ Test git commands after checkout

Implementing these fixes will resolve both authentication errors and branch reference issues in GitHub Copilot workflows.
