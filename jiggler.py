import pyautogui
import time
import logging
import os
import sys

# Define user-writable log path
log_dir = os.path.expanduser("~/Library/Logs/NuclearJiggler")
os.makedirs(log_dir, exist_ok=True)
logfile = os.path.join(log_dir, "jiggler.log")

# Clear previous log at each start
with open(logfile, "w"):
    pass

# Setup logging
logging.basicConfig(
    filename=logfile,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# logging.info("🌀 Nuclear Jiggler started a new session.")

def jiggle():
    try:
        pyautogui.move(1, 0)
        time.sleep(0.5)
        pyautogui.move(-1, 0)
        pyautogui.press('shift')

        msg = "✅ Mouse moved and shift key pressed."
        print(msg)
        logging.info(msg)

    except Exception as e:
        error = f"❌ Error during jiggle: {e}"
        print(error)
        logging.error(error)

jiggle()
