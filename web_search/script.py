import json
import requests
import os

def web_search():
    query = os.getenv('query')
    api_key = os.getenv('api_key')

    if not query or not api_key:
        print("Error: query or api_key environment variables do not exist.")
        return

    payload = json.dumps({
        "q": query
    })
    headers = {
        'X-API-KEY': api_key,
        'Content-Type': 'application/json'
    }
    url = "https://google.serper.dev/search"
    response = requests.request("POST", url, headers=headers, data=payload)
    response = json.loads(response.text)
    organic_items_extracted = [{"link": item["link"], "position": item["position"], "title": item["title"]} for item in response['organic']]
    print(organic_items_extracted)

if __name__ == "__main__":
    web_search()