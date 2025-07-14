import os
import json
import datetime
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow import keras
import subprocess


IMG_HEIGHT = 500
IMG_WIDTH = 500

#path đến model
MODEL_PATH = "path/final_model.h5" 

#path đến chỗ lưu screenshot
SCREENSHOT_DIR = "/home/linh/defe/screenshot" **

#path đến chỗ lưu LOG
LOG_PATH = "/home/linh/defe/log-deface.json"

#Link bạn muốn chụp vd:
URL = "https://www.google.com"


model = keras.models.load_model(MODEL_PATH, compile=False)


os.makedirs(SCREENSHOT_DIR, exist_ok=True)


def get_next_screenshot_path():
    existing_files = [f for f in os.listdir(SCREENSHOT_DIR) if f.endswith(".png")]
    existing_numbers = []
    for f in existing_files:
        try:
            num = int(os.path.splitext(f)[0])
            existing_numbers.append(num)
        except ValueError:
            continue
    next_number = max(existing_numbers, default=0) + 1
    return os.path.join(SCREENSHOT_DIR, f"{next_number}.png")


def take_screenshot(url, output_path):
    command = [
        "google-chrome",
        "--headless",
        "--no-sandbox",
        "--disable-gpu",
        f"--screenshot={output_path}",
        f"--window-size=1280,720",
        url
    ]
    subprocess.run(command, check=True)

def check_defacement(image_path, url):
    img = keras.preprocessing.image.load_img(image_path, target_size=(IMG_HEIGHT, IMG_WIDTH))
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    prediction = model.predict(img_array)
    confidence = float(prediction[0][0])
    result = "defaced" if confidence > 0.5 else "normal"

    print("Canh bao: Trang web co the da bi thay doi (defaced)." if result == "defaced" else "Trang web co ve binh thuong.")

    log_entry = {
        "timestamp": datetime.datetime.now().isoformat(),
        "url": url,
        "result": result,
        "confidence": confidence,
        "screenshot": os.path.basename(image_path)
    }

    try:
        if os.path.exists(LOG_PATH):
            with open(LOG_PATH, "r") as f:
                data = json.load(f)
        else:
            data = []

        data.append(log_entry)

        with open(LOG_PATH, "w") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"Loi ghi log: {e}")


if __name__ == "__main__":
    try:
        screenshot_path = get_next_screenshot_path()
        take_screenshot(URL, screenshot_path)
        check_defacement(screenshot_path, URL)
    except Exception as e:
        print(f"error: {e}")
