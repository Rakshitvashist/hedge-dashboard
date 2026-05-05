# Automated Git Push Script

# Initialize if not already a repo
if (!(Test-Path .git)) {
    Write-Host "Initializing Git repository..."
    git init
    git branch -M main
}

# Check if remote exists, if not ask user or warn
$remote = git remote get-url origin 2>$null
if (!$remote) {
    Write-Warning "No remote 'origin' found. Please run: git remote add origin <URL>"
    exit
}

# Stage all changes
git add .

# Commit with timestamp
$message = "Dashboard Update: " + (Get-Date -Format "yyyy-MM-dd HH:mm:ss")
git commit -m "$message"

# Push to main branch
git push origin main
