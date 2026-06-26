# 🎤 Offline Speech-to-Text Setup

This time study app uses a **local offline speech recognition server** so you can use speech-to-text without internet.

## One-Time Setup (5 minutes)

### 1. Install Python 3
Download from https://www.python.org/downloads/ and install

### 2. Install Dependencies
Open Terminal and run:

```bash
cd /Users/konradandrag/Documents/websites/time\ study\ auto
pip3 install flask flask-cors vosk pyaudio
```

### 3. Download Speech Model
The first time you start the server, it will download the speech recognition model (~50MB):

```bash
python3 -m vosk.download_model
```

## Using the App (Every Time)

### Step 1: Start the Speech Server
Open Terminal and run:

```bash
cd /Users/konradandrag/Documents/websites/time\ study\ auto
python3 speech_server.py
```

You should see:
```
✅ Server starting on http://localhost:5555
✅ Your app can now use speech recognition OFFLINE
⚠️  Keep this terminal window open while using the app
```

### Step 2: Start the Web Server
Open a NEW Terminal tab and run:

```bash
cd /Users/konradandrag/Documents/websites/time\ study\ auto
python3 -m http.server 8000
```

### Step 3: Open the App
Open Chrome and go to:
```
http://localhost:8000/time-study.html
```

### Step 4: Use Speech Recognition
- Click "DO TIME STUDY"
- When on Screen 2 (Recording), speak into your microphone
- Text will appear in the input field automatically

## How It Works

1. **Your app** (time-study.html) captures audio from your microphone
2. **Sends it** to the local speech server (http://localhost:5555)
3. **Server processes it** locally using Vosk (offline speech recognition)
4. **Returns the text** to your app
5. **Everything stays on your computer** - no internet required after setup

## Troubleshooting

**"ModuleNotFoundError: No module named 'vosk'"**
- Run: `pip3 install vosk`

**"Could not open audio device"**
- Make sure your microphone is plugged in and working
- Check macOS Privacy settings: Settings → Privacy & Security → Microphone

**Server won't start**
- Make sure port 5555 is available
- Try: `lsof -i :5555` to see what's using it

**No text appearing when you speak**
- Make sure both servers are running (speech server + web server)
- Check browser console (F12) for errors
- Try speaking more clearly

## Tips

- Keep both terminal windows open while using the app
- Speech takes a second to process - wait after speaking
- Accuracy improves with clear speech
- After initial setup, just restart the two servers next time
