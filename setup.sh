#!/bin/bash

echo "🎤 Setting up Offline Speech-to-Text Server"
echo "=========================================="

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed"
    echo "Please install Python 3 from https://www.python.org/downloads/"
    exit 1
fi

echo "✅ Python 3 found"

# Install required packages
echo ""
echo "📦 Installing required packages..."
pip3 install flask flask-cors vosk pyaudio

# Download Vosk model
echo ""
echo "🤖 Downloading Vosk speech model (first time only)..."
python3 -m vosk.download_model

echo ""
echo "✅ Setup complete!"
echo ""
echo "To start the speech server, run:"
echo "  python3 speech_server.py"
echo ""
echo "Then open http://localhost:8000/time-study.html in your browser"
