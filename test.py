import json
import serpapi

#https://serpapi.com/playground?engine=google_finance&q=GOOGL%3ANASDAQ&hl=pt-br&window=1D
#https://serpapi.com/google-finance-api

with open("config.json", "r") as config_file:
    config = json.load(config_file)

client = serpapi.Client(api_key=config["api_key"])

results = client.search({
  "engine": "google_finance",
  "q": "GOOGL:NASDAQ",
  "hl": "pt-br",
  "window": "1D"
})

with open("results.json", "w") as file:
    json.dump(results.data, file, indent=2)
    
