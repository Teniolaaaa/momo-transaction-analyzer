# Fix commit messages
cd C:\Users\LENOVO\momo-transaction-analyzer

# Set environment to avoid interactive editors
$env:GIT_EDITOR = "true"

# Create a temporary branch
git checkout -b temp-fix

# Reset to keep changes but remove commits
git reset --soft HEAD~7

# Create new commits with natural messages
git commit -m "Add project files and setup"
Write-Host "Created first commit"

# Push with force
git push origin temp-fix -f

# Switch back to main and update
git checkout main
git reset --hard temp-fix
git push origin main -f

# Delete temp branch
git branch -D temp-fix

Write-Host "Done! Check your GitHub now."
