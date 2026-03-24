import json
import serpapi

#https://serpapi.com/playground?engine=google_finance&q=GOOGL%3ANASDAQ&hl=pt-br&window=1D
#https://serpapi.com/google-finance-api


client = serpapi.Client(api_key="3ea5d182282942a7355b9d38a88bf0dccb2ffd7b7211e104027260dba406c51f")
results = client.search({
  "engine": "google_finance",
  "q": "GOOGL:NASDAQ",
  "hl": "pt-br",
  "window": "1D"

})

with open("results.json", "w") as file:
    json.dump(results.data, file, indent=2) 
