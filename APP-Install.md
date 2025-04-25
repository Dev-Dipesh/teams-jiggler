# Applescript Exported App Instructions

> ⚠️ The script runs in endless loop and requires force quit.

## 📦 Step 1: Set Up the Project

If you haven’t already:

```bash
git clone https://github.com/your-username/nuclear-jiggler.git
cd nuclear-jiggler
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 🛠 Step 2: Export the AppleScript

1. Open `jiggler.applescript` in the **Script Editor** app (search via Spotlight)
2. Go to `File > Export…`
3. Choose:
   - **File Format:** Application
   - **Name:** `Nuclear Jiggler.app`
   - **Location:** Anywhere (e.g. Desktop or inside the repo folder)

---

## 🔒 Step 3: Grant Accessibility Permissions

Go to:

> **System Settings > Privacy & Security > Accessibility**

- Click the ➕ button and add your exported `Nuclear Jiggler.app`
- Make sure it is checked ✅

This allows the app to simulate mouse/keyboard actions.

---

## 🚀 Step 4: Run It

Double-click `Nuclear Jiggler.app`. It will:

- Start running silently in the background
- Simulate activity every few minutes
- Prevent Teams (and similar tools) from marking you as Away

To stop it: use **⌘ + Q** or **Force Quit** from the Dock.

---

## 📁 Optional: Add to Login Items

To make it launch automatically:

1. Go to `System Settings > General > Login Items`
2. Click `+` and add `Nuclear Jiggler.app`

Done! Now it runs every time you log in 🎉

---

## 🧼 Notes

- Make sure `venv` and dependencies stay in the same folder if you move the app
- If you move it elsewhere, re-check that the script path still works

---

Built with 💻 Python, ☢️ nuclear intent, and 💪 determination.
