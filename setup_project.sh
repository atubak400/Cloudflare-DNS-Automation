#!/bin/bash

# Create main project folder
mkdir Cloudflare-DNS-Automation
cd Cloudflare-DNS-Automation

# Create main files
touch README.md requirements.txt config.yaml dns_automation.py security_enforcement.py monitoring.py .gitignore

# Create folders
mkdir logs reports

# Add default content into .gitignore
echo "config.yaml" >> .gitignore
echo "logs/" >> .gitignore
echo "reports/" >> .gitignore
echo "__pycache__/" >> .gitignore
echo "*.pyc" >> .gitignore

echo "✅ Project folder structure created successfully!"
