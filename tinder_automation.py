import uiautomator2 as u2
import time

# Connect to the device
device = u2.connect()

# Launch Tinder (make sure Tinder is installed)
device.app_start("com.tinder")

# Wait for the app to load
time.sleep(10)

# Function to swipe right (like)
def swipe_right():
    device.swipe_ext("right", scale=0.8)
    time.sleep(2)  # Add a delay to mimic human interaction

# Function to swipe left (unlike)
def swipe_left():
    device.swipe_ext("left", scale=0.8)
    time.sleep(2)  # Add a delay to mimic human interaction

# Function to perform swipes in a loop
def automate_tinder_swipes(n):
    for _ in range(n):
        swipe_right()
        # Uncomment the line below if you want to alternate swipes
        # swipe_left()

# Automate Tinder swipes (e.g., swipe right 10 times)
automate_tinder_swipes(10)

# Close Tinder after automation
device.app_stop("com.tinder")
