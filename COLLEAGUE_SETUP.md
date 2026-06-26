# 👥 Colleague Setup Guide

Your colleague has set up a **Time Study App** for you to use! Here's how to get it running in 3 minutes.

## Step 1: Clone the Repository

```bash
git clone https://github.com/konradandrag-max/time-study-auto.git
cd time-study-auto
```

## Step 2: Install Dependencies (One-time)

```bash
bash setup.sh
```

This installs: `flask`, `flask-cors`, `vosk` (offline speech recognition)

## Step 3: Start the Speech Server

```bash
python3 speech_server.py
```

You should see:
```
✅ Server starting on http://localhost:5555
✅ Your app can now use speech recognition OFFLINE
⚠️  Keep this terminal window open while using the app
```

## Step 4: Open the Web App

Open your browser and go to:

👉 **https://konradandrag-max.github.io/time-study-auto/time-study.html**

That's it! Your app is ready to use. 🎉

---

## Using the App

1. **Configure Settings** (first time only)
   - Set your operator name, work centre, and performance rating

2. **Start a Time Study**
   - Click "DO TIME STUDY" button

3. **Record Activities**
   - Speak into your microphone to log activities
   - App transcribes speech automatically (offline)
   - No internet needed!

4. **Review & Save**
   - Review your activities before saving
   - Click to edit individual activities if needed

5. **Edit Saved Studies**
   - Go to Dashboard to view your saved studies
   - Click on any study to edit activities, ratings, and details
   - Changes are saved automatically

6. **View Analytics**
   - Dashboard shows your efficiency trends
   - Export data as CSV or JSON

---

## Troubleshooting

**Python not found?**
- Install Python 3: https://www.python.org/downloads/

**"ModuleNotFoundError: No module named 'vosk'"?**
```bash
pip3 install flask flask-cors vosk
```

**No microphone access?**
- Check browser permissions (allow microphone)
- macOS: Settings → Privacy & Security → Microphone

**Can't connect to web app?**
- Make sure speech server is running in terminal
- Try refreshing the browser

**Questions?**
- Ask your colleague (Konrad)

---

## Data Privacy

✅ **Your data stays on YOUR computer** — all data is stored in your browser's local storage
✅ **Offline by default** — no internet needed after initial setup
✅ **No account required** — just start using it

Enjoy! 📊⏱️
