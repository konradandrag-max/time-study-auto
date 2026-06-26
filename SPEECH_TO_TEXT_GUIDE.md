# 🎤 Speech-to-Text Installation Guide

This guide will help you set up **offline speech recognition** for the Time Study App. Everything runs on YOUR computer—no internet needed!

---

## **What You Need**

- **Python 3** (free download)
- **Your microphone**
- **Terminal/Command Prompt**

---

## **Step 1: Install Python 3**

### macOS or Windows:
1. Go to: https://www.python.org/downloads/
2. Download **Python 3.11 or newer**
3. Run the installer
4. ✅ Check "Add Python to PATH" during installation
5. Click **Install**

### Already have Python?
Open Terminal/Command Prompt and type:
```bash
python3 --version
```
If you see `Python 3.x.x`, you're good! Skip to **Step 2**.

---

## **Step 2: Install Speech Recognition Libraries**

Open Terminal (Mac) or Command Prompt (Windows) and run:

```bash
pip3 install flask flask-cors vosk
```

Wait for it to finish. You should see:
```
Successfully installed flask flask-cors vosk
```

✅ **Done!** You now have offline speech recognition installed.

---

## **Step 3: Start the Speech Server (Every Time You Use the App)**

Each time you want to use the Time Study App:

1. **Open Terminal (Mac) or Command Prompt (Windows)**

2. **Navigate to the app folder:**
   ```bash
   cd /path/to/time-study-auto
   ```
   (Replace `/path/to/` with wherever you cloned the repo)

3. **Start the speech server:**
   ```bash
   python3 speech_server.py
   ```

4. **You should see:**
   ```
   ✅ Server starting on http://localhost:5555
   ✅ Your app can now use speech recognition OFFLINE
   ⚠️  Keep this terminal window open while using the app
   ```

✅ **The speech server is now running!**

---

## **Step 4: Use the App**

1. **Keep the Terminal window OPEN** (the one running `speech_server.py`)

2. **Open your browser** and go to:
   ```
   https://konradandrag-max.github.io/time-study-auto/time-study.html
   ```

3. **Click "DO TIME STUDY"** and start speaking!

The app will automatically transcribe your speech. 🎉

---

## **Troubleshooting**

### **"Python not found"**
- Make sure you installed Python and checked "Add to PATH"
- Restart your Terminal/Command Prompt
- Try: `python --version` (instead of `python3`)

### **"ModuleNotFoundError: No module named 'vosk'"**
```bash
pip3 install vosk
```

### **"Permission denied" on macOS?**
Try:
```bash
pip3 install --user vosk
```

### **Microphone not working?**
1. Check your microphone is plugged in
2. **macOS:** Settings → Privacy & Security → Microphone (allow the app)
3. **Windows:** Settings → Privacy & Security → Microphone (allow)

### **No text appearing when I speak?**
- Make sure the Terminal window with `speech_server.py` is OPEN
- Speak clearly and wait 1-2 seconds
- Check browser console: Press `F12`, look for errors

### **"Port 5555 already in use"**
Another app is using that port. Try:
```bash
# macOS/Linux:
lsof -i :5555

# Windows:
netstat -ano | findstr :5555
```
Close that app or contact Konrad.

---

## **How It Works**

```
Your Microphone
       ↓
   Your Browser (captures audio)
       ↓
   Speech Server (on your computer)
       ↓
   Vosk Speech Recognition (offline)
       ↓
   Text appears in the app
```

✅ **Everything stays on your computer—totally private!**

---

## **Tips**

- Keep both the **Terminal window** and **browser** open while using the app
- Speech takes 1-2 seconds to process after you finish speaking
- Clear speech = better accuracy
- You only need to install step 1-2 ONCE. After that, just run step 3 each time.

---

## **Still Having Issues?**

Ask **Konrad**—he can help!

Enjoy your offline speech-to-text! 🎤✨
