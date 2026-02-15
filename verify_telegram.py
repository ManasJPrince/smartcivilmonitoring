import requests

# User provided: -8547426960:AAFqzeQkgt_R-jDL26pdStX_3asPMfbnR8s
# The '-' might be a typo, or it's a Chat ID mixed with a token. 
# Standard Token format: 123456789:AbCdEfGhIjKlMnOpQrStUvWxYz
# Let's try removing the leading '-' first.

POSSIBLE_TOKEN = "8547426960:AAFqzeQkgt_R-jDL26pdStX_3asPMfbnR8s"

def test_token(token):
    print(f"Testing token: {token[:15]}...")
    url = f"https://api.telegram.org/bot{token}/getMe"
    try:
        resp = requests.get(url)
        data = resp.json()
        if data.get("ok"):
            print(f"SUCCESS! Bot Name: {data['result']['first_name']} (@{data['result']['username']})")
            return True
        else:
            print(f"Failed: {data.get('description')}")
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False

success = test_token(POSSIBLE_TOKEN)

if not success:
    # Try with the minus sign just in case (though unlikely for a token ID)
    test_token("-8547426960:AAFqzeQkgt_R-jDL26pdStX_3asPMfbnR8s")
