import requests
import time

TOKEN = "8547426960:AAFqzeQkgt_R-jDL26pdStX_3asPMfbnR8s"

def get_updates():
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    try:
        resp = requests.get(url)
        data = resp.json()
        if not data.get("ok"):
            print(f"Error: {data}")
            return

        updates = data.get("result", [])
        if not updates:
            print("No new messages found. Please send '/start' to your bot @UrbanWatch_Bot now!")
            return

        last_msg = updates[-1]
        chat_id = last_msg["message"]["chat"]["id"]
        user = last_msg["message"]["from"]["first_name"]
        
        print(f"\nSUCCESS! Found a message from {user}.")
        print(f"YOUR CHAT ID IS: {chat_id}")
        print("Please copy this number and paste it to the AI.")
        
    except Exception as e:
        print(f"Error: {e}")

print("Checking for messages...")
get_updates()
