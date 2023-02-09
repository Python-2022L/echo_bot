import requests
from pprint import pprint
from time import sleep
TOKEN = '5661659754:AAHjcXFhVC9UdI0Q83YBMReNptJXBXFFESs'

def get_updates():
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    response = requests.get(url)
    data = response.json() 
    return data['result']

def get_last_updates(result):
    """
    Use this function to get updates from Telegram.

    Args:
        None
    Returns:
        int(chat_id): Telegram chat id
        str(text): Message text
        int(update_id): Telegram update id
    """ 
    message = result[-1]
    update_id = message['update_id']
    chat_id = message['message']['chat']['id']
    text = message['message']['text']

    return chat_id, text, update_id

def send_message(chat_id, text):
    """
    Use this function to send text messages.

    Args:
        chat_id (int): Telegram chat id
        text (str): Message text
    Returns:
        None
    """
    params = {
        "chat_id": chat_id,
        "text": text
    }
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    response = requests.get(url, params=params)
    data = response.json()
    return data

last_update_id = -1

while True:
    result = get_updates()
    chat_id, text, update_id = get_last_updates(result)
    print(f"LAST_UPDATE:{last_update_id} \t UPDATE: {update_id}")
    if update_id != last_update_id:
        if text == '/start':
            send_message(chat_id, "Echo Botga hush kelibsiz")
        else:
            send_message(chat_id, text)
        last_update_id = update_id
    sleep(2)

