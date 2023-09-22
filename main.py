import requests
import json
url = "https://twelve-data1.p.rapidapi.com/time_series"

querystring = {"symbol":"AMZN","interval":"1day","outputsize":"30","format":"json"}

headers = {
	"X-RapidAPI-Key": "e8aa58d0a5msh6950ea6600e16bfp1bde78jsn52b2fd234052",
	"X-RapidAPI-Host": "twelve-data1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
data =response.json()
test = json.dumps(data)

import requests

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IBM&outputsize=full&apikey=demo'
r = requests.get(url)
data = r.json()

print(data)
pass