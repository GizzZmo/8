# Quick Start: Setting Up GitHub Secrets for Copilot Workflows

This guide provides step-by-step instructions for configuring GitHub secrets to fix authentication errors.

## Prerequisites

- Repository admin or write access
- GitHub account with Copilot enabled

## Step 1: Generate a Personal Access Token

1. Click your profile picture (top-right) → **Settings**
2. Scroll down to **Developer settings** (bottom-left)
3. Click **Personal access tokens** → **Tokens (classic)**
4. Click **Generate new token (classic)**
5. Configure your token:
   - **Note**: `Copilot Workflow Token` (or any descriptive name)
   - **Expiration**: Choose an appropriate duration (90 days recommended)
   - **Select scopes**:
     - ✅ `repo` (Full control of private repositories)
     - ✅ `workflow` (Update GitHub Action workflows)
     - ✅ `read:org` (Read organization membership) - if applicable
6. Click **Generate token**
7. **IMPORTANT**: Copy the token immediately - you won't see it again!

## Step 2: Add Token to Repository Secrets

1. Navigate to your repository: `https://github.com/GizzZmo/8`
2. Click **Settings** (repository settings, not user settings)
3. In the left sidebar, click **Secrets and variables** → **Actions**
4. Click **New repository secret**
5. Configure the secret:
   - **Name**: `COPILOT_TOKEN`
   - **Secret**: Paste the token you copied in Step 1
6. Click **Add secret**

## Step 3: Verify Secret Configuration

After adding the secret, you should see it listed under "Repository secrets":

```
COPILOT_TOKEN
Updated: Just now
```

**Note**: The actual value will be hidden for security.

## Step 4: Test the Configuration

### Option A: Trigger Workflow Manually

1. Go to **Actions** tab in your repository
2. Select the workflow (e.g., "Copilot Agent Example")
3. Click **Run workflow** dropdown
4. Click **Run workflow** button
5. Check the workflow run logs to verify no 401 errors

### Option B: Create a Pull Request

1. Create a new branch with a small change
2. Open a pull request
3. The workflow should trigger automatically
4. Check the workflow run in the PR's "Checks" tab

## Step 5: Verify No Authentication Errors

In the workflow logs, you should see:

✅ **Good** (No authentication errors):
```
Checkout code
Verify main branch exists
Compare with main branch
Example Copilot API interaction
COPILOT_TOKEN is configured
```

❌ **Bad** (Authentication errors - secret not configured properly):
```
401 Unauthorized: unauthorized: AuthenticateToken authentication failed
Failed to list models: 401 Unauthorized
```

## Common Issues and Solutions

### Issue: "Secret not found" error

**Solution**: Ensure the secret name is exactly `COPILOT_TOKEN` (case-sensitive)

### Issue: Still getting 401 errors after adding secret

**Possible causes**:
1. Token expired - regenerate a new token
2. Missing scopes - ensure `repo` and `workflow` are selected
3. Token revoked - check token status in Settings → Developer settings
4. Wrong organization - ensure token is for the correct org/user

**Solution**: 
- Delete the old secret
- Generate a new token with correct scopes
- Add the new token as a secret

### Issue: Workflow doesn't trigger

**Possible causes**:
1. Workflow file syntax error
2. Wrong branch
3. Event trigger not configured

**Solution**:
- Validate YAML syntax: `yamllint .github/workflows/*.yml`
- Check branch name in workflow file
- Verify `on:` section includes the correct events

## Security Reminders

⚠️ **NEVER**:
- Commit tokens directly in code
- Share tokens in chat/email
- Use the same token across multiple services
- Give tokens more permissions than needed

✅ **ALWAYS**:
- Store tokens in GitHub Secrets
- Use descriptive names for tokens
- Set expiration dates
- Revoke unused or old tokens
- Rotate tokens regularly (every 90 days)

## Need More Help?

See the comprehensive guide: [COPILOT_AUTHENTICATION_FIX.md](COPILOT_AUTHENTICATION_FIX.md)

## Summary Checklist

- [ ] Generated personal access token with `repo` and `workflow` scopes
- [ ] Added `COPILOT_TOKEN` to repository secrets
- [ ] Verified secret is listed in repository settings
- [ ] Tested workflow run - no 401 errors
- [ ] All branches are accessible (main branch not missing)

If all items are checked, your repository is properly configured! 🎉
