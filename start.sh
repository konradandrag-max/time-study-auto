#!/bin/bash

# This script starts both the speech server and web server for the Time Study app

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

echo "🎤 Digital Time Study - Offline Speech-to-Text"
echo "=============================================="
echo ""
echo "This will start:"
echo "  1. Speech-to-Text server (port 5555)"
echo "  2. Web server (port 8000)"
echo ""

# Check if Python3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed"
    echo "Please install from https://www.python.org/downloads/"
    exit 1
fi

echo "✅ Checking speech server..."
if python3 speech_server.py &
    SPEECH_PID=$!
    sleep 2

    if curl -s http://localhost:5555/health > /dev/null 2>&1; then
        echo "✅ Speech server is running on port 5555"
    else
        echo "⚠️ Speech server may not have started. Check output above."
    fi
fi

echo ""
echo "✅ Starting web server on port 8000..."
echo ""
echo "📱 Open Chrome and go to: http://localhost:8000/time-study.html"
echo ""
echo "Press Ctrl+C to stop both servers"
echo ""

python3 -m http.server 8000 --bind 127.0.0.1
