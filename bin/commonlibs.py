import requests
from datetime import datetime
import pytz


def getCityWeatherDetails(cityName):
    name = cityName

    # Enter your API Key from Openweathermap API
    apikey = "<Enter your API Key>"

    # OpenWeathermap API URL Details
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

    response = requests.get(url.format(name, apikey))

    if response.status_code == 200:
        return response.json()
    else:
        print("Incorrect Details Passed to URL and Hence Failed to Fetch the response: ", response)
        return None


def convertTimestamp(stamp):

    # converting unix timestamp to datetime object
    dt = datetime.fromtimestamp(stamp)

    # Set the timezone to Indian Time zone
    indian_tz = pytz.timezone("Asia/Kolkata")
    dt_ist = dt.astimezone(indian_tz)

    ist_str = dt_ist.strftime('%Y-%m-%d %H-%M-%S %Z %z')

    return ist_str
