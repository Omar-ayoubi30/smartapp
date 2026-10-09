import json
import urllib.request
import urllib.error


def live_weer():
    """Haalt live weerdata op voor Utrecht via de Open-Meteo API."""
    # Coördinaten van Utrecht: Latitude 52.0908, Longitude 5.1222
    url = "https://api.open-meteo.com/v1/forecast?latitude=52.0908&longitude=5.1222&current_weather=true"

    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'SmartApp/1.0'})
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode('utf-8'))
            temp = data["current_weather"]["temperature"]
            wind = data["current_weather"]["windspeed"]
            return {"succes": True, "temp": temp, "wind": wind}

    except urllib.error.URLError:
        return {"succes": False, "fout": "Geen internetverbinding of API onbereikbaar."}
    except Exception as e:
        return {"succes": False, "fout": f"Onverwachte fout: {e}"}