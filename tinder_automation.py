import uiautomator2 as u2
import time
import random
import os
import psycopg2
from datetime import datetime

# Function to connect to PostgreSQL
def connect_db():
    conn = psycopg2.connect(
        dbname="your_dbname",
        user="your_user",
        password="your_password",
        host="your_host",
        port="your_port"
    )
    print("Connected to the database successfully.")
    return conn

# Function to log actions to PostgreSQL
def log_action(conn, action):
    cur = conn.cursor()
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cur.execute(
        "INSERT INTO tinder_logs (action, timestamp) VALUES (%s, %s)",
        (action, timestamp)
    )
    conn.commit()
    cur.close()
    print(f"Logged action: {action} at {timestamp}")

# Function to run the Tinder automation script
def run_tinder_automation(conn):
    device = u2.connect()
    device.app_start("com.tinder")
    time.sleep(10)

    def random_delay(min_delay=2, max_delay=5):
        delay = random.uniform(min_delay, max_delay)
        print(f"Waiting for {delay:.2f} seconds...")
        time.sleep(delay)

    def swipe_right():
        os.system("adb shell input swipe 800 1000 100 1000")
        log_action(conn, "Like")
        random_delay()

    def swipe_left():
        os.system("adb shell input swipe 100 1000 800 1000")
        log_action(conn, "Dislike")
        random_delay()

    def automate_tinder_swipes(n):
        for i in range(n):
            # 70% chance to swipe right (like), 30% chance to swipe left (dislike)
            if random.random() < 0.7:
                swipe_right()
            else:
                swipe_left()

            if random.random() < 0.1:  # 10% chance to take a break
                break_time = random.randint(10, 20)
                print(f"Taking a short break for {break_time} seconds...")
                time.sleep(break_time)

    automate_tinder_swipes(20)
    device.app_stop("com.tinder")
    print("Tinder app stopped.")
    log_action(conn, "App Restart")

if __name__ == "__main__":
    conn = connect_db()
    while True:
        try:
            run_tinder_automation(conn)
        except Exception as e:
            print(f"An error occurred: {e}. Restarting the automation...")
            log_action(conn, "App Error")
            time.sleep(5)
    
    conn.close()