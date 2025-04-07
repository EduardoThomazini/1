import requests
import os

from dotenv import load_dotenv

# carrega a .env
load_dotenv()

# variaveis de ambiente
api_key = os.getenv("API_KEY")
cidade = os.getenv("CIDADE")
parametros = os.getenv("PARAMS")

headers = {
    "Transfer-Encoding": "chunked",
    "Connection": "keep-alive",
    "Vary": "Accept-Encoding",
    "CDN-PullZone": "93447",
    "CDN-Uid": "8fa3a04a-75d9-4707-8056-b7b33c8ac7fe",
    "CDN-RequestCountryCode": "GB",
    "x-weatherapi-qpm-left": "5000000",
    "CDN-ProxyVer": "1.22",
    "CDN-RequestPullSuccess": "True",
    "CDN-RequestPullCode": "200",
    "CDN-CachedAt": "04/07/2025 23:30:32",
    "CDN-EdgeStorageId": "864",
    "CDN-RequestId": "87796449d7777442976018fbae33177d",
    "CDN-Cache": "MISS",
    "CDN-Status": "200",
    "CDN-RequestTime": "0",
    "Cache-Control": "public, max-age=180",
    "Content-Type": "application/json",
    "Date": "Mon, 07 Apr 2025 23:30:32 GMT",
    "Server": "BunnyCDN-DE1-722"
    }

url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={cidade}&aqi={parametros}'

# faz a request
response = requests.get(url, headers=headers)

# verifica como foi a resposta
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
    print(response.text)
