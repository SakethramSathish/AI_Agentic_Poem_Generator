import os
import requests

def upload_to_pastebin(poem: str, title: str = "Untitled Poem") -> str:
    api_dev_key = os.getenv("PASTEBIN_API_KEY")
    if not api_dev_key:
        raise ValueError("Pastebin API Key not found in the .env file.")
    
    data = {
        "api_dev_key": api_dev_key,
        "api_option": "paste",
        "api_paste_code": poem,
        "api_paste_name": title,        
        "api_paste_private": 1,         #0 - Public, 1 - Unlisted, 2 - Private
        "api_paste_expiry_date": "N"    #No expiry date
    }

    response = requests.post("https://pastebin.com/api/api_post.php", data=data)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to upload poem: {response.status_code} - {response.text}")