import uiautomator2 as u2
import time
import random
import os

# Connect to the device
device = u2.connect()

# Launch Tinder (make sure Tinder is installed)
device.app_start("com.tinder")

# Wait for the app to load
time.sleep(10)

# Function to simulate a random delay
def random_delay(min_delay=2, max_delay=5):
    delay = random.uniform(min_delay, max_delay)
    time.sleep(delay)

# Function to swipe right (like)
def swipe_right():
    os.system("adb shell input swipe 800 1000 100 1000")
    random_delay()

# Function to swipe left (unlike)
def swipe_left():
    os.system("adb shell input swipe 100 1000 800 1000")
    random_delay()

# Function to simulate human-like swiping behavior
def automate_tinder_swipes(n):
    for _ in range(n):
        action = random.choice([swipe_right, swipe_left, lambda: time.sleep(random.uniform(2, 5))])
        action()
        
        # Randomly take breaks
        if random.random() < 0.1:  # 10% chance to take a break
            print("Taking a short break...")
            time.sleep(random.randint(10, 20))  # Break for 10-20 seconds



# Automate Tinder swipes (e.g., swipe 20 times)
automate_tinder_swipes(20)

# Close Tinder after automation
device.app_stop("com.tinder")
