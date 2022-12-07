import requests

# Get the weather report.
def WeatherReport(City="Bhagalpur"):
    # https://medium.com/analytics-vidhya/forecast-weather-using-python-e6f5519dc3c1
    print(f"Displaying weather report for: {City}")

    # Fetch weather details.
    URL = f"https://wttr.in/{City}?format=%C"
    res = requests.get(URL)

    return res.text
