import requests
import os 
from dotenv import load_dotenv

import json

load_dotenv()

AUTH_ENDPOINT ="https://id.twitch.tv/oauth2/token"
SUB_ENDPOINT = 'https://api.twitch.tv/helix/eventsub/subscriptions'

def authenticate():

    AutParams = {'client_id': f"{os.getenv('TWITCH_CLIENT_ID')}"
    , 'client_secret': f"{os.getenv('TWITCH_SECRET')}"
    , 'grant_type': 'client_credentials'}

    print("REQUESTING ACCESS TOKEN")

    AutCall = requests.post(url=AUTH_ENDPOINT, params=AutParams)

    auth_resp = AutCall.json()
    access_token = auth_resp['access_token']

    print(access_token)

    return access_token

def make_sub(access_token):

    payload = {
        "type": "channel.follow",
        "version": "1",
        "condition": {
            "broadcaster_user_id": "12826"
        },
        "transport": {
            "method": "webhook",
            "callback": f"{os.getenv('TUNNEL_URL')}",
            "secret": "s3cRe7s3cRe7"
        }
    }

    headers = {"Client-ID": f"{os.getenv('TWITCH_CLIENT_ID')}",
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"}

    r = requests.post(SUB_ENDPOINT,headers=headers, data= json.dumps(payload))

    print(r.json())

    return r.json()

def get_subs(access_token):

    headers = {"Client-ID": f"{os.getenv('TWITCH_CLIENT_ID')}",
    "Authorization": f"Bearer {access_token}"}

    r = requests.get(SUB_ENDPOINT,headers=headers)
    print(r.json())
    return r.json()

access_token = authenticate()
get_subs(access_token)