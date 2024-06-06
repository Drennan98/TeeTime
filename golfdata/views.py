from django.shortcuts import render
import requests

# Create your views here.

def fetch_data():
    # Code snippet taken from rapidapi website (Live Golf Data API)
    api_key = "e88b72e5bcmshecbea79dc8bf4f7p15662bjsn9e1deb143c51"
    url = "https://live-golf-data.p.rapidapi.com/schedule"
    querystring = {"orgId":"1","year":"2024"}
    headers = {
        "x-rapidapi-key": "e88b72e5bcmshecbea79dc8bf4f7p15662bjsn9e1deb143c51",
        "x-rapidapi-host": "live-golf-data.p.rapidapi.com"
    }
    
    response = requests.get(url, headers=headers, params=querystring)


def live_scores(request):
        data = fetch_data()
        return render(request, 'golfdata/golf_scoring.html', {'data': data})