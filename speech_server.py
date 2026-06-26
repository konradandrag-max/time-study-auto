#!/usr/bin/env python3
"""
Offline speech-to-text server using Vosk
Requires: pip3 install vosk flask flask-cors
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import sys
import vosk
import urllib.request
import os

app = Flask(__name__)
CORS(app, origins="*")

# Download model if not present
MODEL_PATH = "model"
if not os.path.exists(MODEL_PATH):
    print("📥 Downloading Vosk speech model (first time only)...")
    try:
        model_url = "https://alphacephei.com/vosk/models/vosk-model-en-us-0.22.zip"
        urllib.request.urlretrieve(model_url, "model.zip")
        import zipfile
        with zipfile.ZipFile("model.zip", 'r') as zip_ref:
            zip_ref.extractall()
        os.rename("vosk-model-en-us-0.22", MODEL_PATH)
        os.remove("model.zip")
        print("✅ Model downloaded successfully")
    except Exception as e:
        print(f"❌ Error downloading model: {e}")
        sys.exit(1)

# Load model
try:
    model = vosk.Model(MODEL_PATH)
    print("✅ Vosk model loaded successfully")
except Exception as e:
    print(f"❌ Error loading Vosk model: {e}")
    sys.exit(1)

@app.route('/health', methods=['GET'])
def health():
    """Check if server is running"""
    return jsonify({'status': 'ok', 'message': 'Speech server is running offline'})

@app.route('/transcribe', methods=['POST'])
def transcribe():
    """
    Receive audio and transcribe it
    Expected: audio/wav file in request
    Returns: {'transcript': 'transcribed text'}
    """
    try:
        audio_data = request.data

        if not audio_data:
            return jsonify({'error': 'No audio data provided'}), 400

        # Create recognizer
        rec = vosk.KaldiRecognizer(model, 16000)

        # Process audio
        try:
            rec.AcceptWaveform(audio_data)
        except Exception as e:
            return jsonify({'error': f'Invalid audio format: {str(e)}'}), 400

        # Get final result
        result_str = rec.FinalResult()
        result = json.loads(result_str)

        transcript = result.get('result', [])
        if transcript:
            text = ' '.join([item['result'] for item in transcript if 'result' in item])
        else:
            text = result.get('partial', '')

        return jsonify({
            'transcript': text,
            'confidence': 'high' if transcript else 'low'
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("=" * 60)
    print("🎤 OFFLINE SPEECH-TO-TEXT SERVER")
    print("=" * 60)
    print("\n✅ Server starting on http://localhost:5555")
    print("✅ Your app can now use speech recognition OFFLINE")
    print("\n📱 Open your time study app and it will connect automatically")
    print("\n⚠️  Keep this terminal window open while using the app")
    print("\nPress Ctrl+C to stop the server\n")
    print("=" * 60)

    app.run(host='127.0.0.1', port=5555, debug=False)
