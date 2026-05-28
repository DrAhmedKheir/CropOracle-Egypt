# GitHub Upload Guide

This guide explains how to upload **CropOracle Egypt** to your GitHub account.

## Option A — Upload using GitHub website

1. Go to GitHub.
2. Create a new repository named:

```text
CropOracle-Egypt
```

3. Add this repository description:

```text
WhatsApp-based multi-agent AI system for APSIM Next Gen wheat simulations and climate-smart advisory services for Egyptian farmers.
```

4. Keep the repository public or private depending on your plan.
5. Do not initialize with README if you are uploading this prepared folder, because the folder already includes a README.
6. Upload all files from this project folder.
7. Commit with this message:

```text
Initial release of CropOracle Egypt multi-agent APSIM advisory system
```

## Option B — Upload using Git command line

From inside the project folder:

```bash
git init
git add .
git commit -m "Initial release of CropOracle Egypt multi-agent APSIM advisory system"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/CropOracle-Egypt.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username.

## Recommended GitHub topics

Add these topics to improve discoverability:

```text
apsim
crop-modeling
wheat
egypt
agritech
climate-smart-agriculture
whatsapp-bot
multi-agent-ai
flask
langgraph
decision-support-system
precision-agriculture
```

## Suggested repository sections

After uploading, enable:

- Issues
- Discussions
- Wiki, optional
- GitHub Actions, later for automated testing

## Important security notes

Never upload:

- `.env`
- API keys
- WhatsApp tokens
- APSIM paid/protected data if any
- Farmer personal information
- Private field trial datasets without permission

This repository includes `.env.example` only. Real credentials should remain local or be stored as GitHub Secrets during deployment.
