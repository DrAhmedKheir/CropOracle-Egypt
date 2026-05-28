#!/usr/bin/env bash
set -e

# Usage:
# bash scripts/upload_to_github.sh YOUR_USERNAME CropOracle-Egypt

USERNAME=${1:-YOUR_USERNAME}
REPO=${2:-CropOracle-Egypt}

if [ "$USERNAME" = "YOUR_USERNAME" ]; then
  echo "Please provide your GitHub username:"
  echo "bash scripts/upload_to_github.sh YOUR_USERNAME CropOracle-Egypt"
  exit 1
fi

git init
git add .
git commit -m "Initial release of CropOracle Egypt multi-agent APSIM advisory system"
git branch -M main
git remote add origin "https://github.com/${USERNAME}/${REPO}.git"
git push -u origin main
