#!/bin/bash
# Installation script for Gemini Master FPS Game AI

set -e

echo "============================================================"
echo "Gemini Master - FPS Game AI Installation"
echo "============================================================"
echo ""

# Check Python version
echo "Checking Python version..."
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "Found Python $python_version"

required_version="3.8"
if [[ $(echo -e "$python_version\n$required_version" | sort -V | head -n1) != "$required_version" ]]; then
    echo "Error: Python 3.8 or higher is required"
    exit 1
fi
echo "✓ Python version OK"
echo ""

# Create virtual environment
echo "Creating virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✓ Virtual environment created"
else
    echo "✓ Virtual environment already exists"
fi
echo ""

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate
echo "✓ Virtual environment activated"
echo ""

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip -q
echo "✓ pip upgraded"
echo ""

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt -q
echo "✓ Dependencies installed"
echo ""

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    echo "Creating .env file from template..."
    cp .env.example .env
    echo "✓ .env file created"
    echo ""
    echo "⚠ IMPORTANT: Edit .env and add your GEMINI_API_KEY"
    echo "   Get your key from: https://aistudio.google.com/app/apikey"
else
    echo "✓ .env file already exists"
fi
echo ""

# Run setup test
echo "Running setup test..."
python test_setup.py
echo ""

echo "============================================================"
echo "Installation Complete!"
echo "============================================================"
echo ""
echo "Next steps:"
echo "1. Edit .env and add your GEMINI_API_KEY"
echo "2. Read README.md for usage instructions"
echo "3. Run: python main.py"
echo ""
echo "To activate the virtual environment later:"
echo "  source venv/bin/activate"
echo ""
