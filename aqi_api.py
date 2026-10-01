import requests
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))
token = os.getenv("API_KEY")

def get_aqi(city):
    url = f"https://api.waqi.info/feed/{city}/?token={token}"
    response = requests.get(url)
    data = response.json()

    if data["status"] != "ok":
        return None

    result = data["data"]
    print(data)

    return {
        "city": result["city"]["name"],
        "aqi": result["aqi"],
        "dominant_pollutant": result.get("dominentpol", "N/A"),
        "updated_at": result["time"]["s"]
    }
