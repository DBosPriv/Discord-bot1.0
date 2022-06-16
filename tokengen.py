import requests

API_URL = "https://osu.ppy.sh/api/v2"
TOKEN_URL = "https://osu.ppy.sh/oauth/token"

def tokengen():
    data = {
        'client_id': 15152,
        'client_secret': '',
        'grant_type': 'client_credentials',
        'scope': 'public'
    }

    response = requests.post(TOKEN_URL,data=data)

    return response.json().get('access_token')

def osuapi(params,link):
    token = tokengen()

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    response = requests.get(f'{API_URL}/{link}', params=params, headers=headers)

    return response