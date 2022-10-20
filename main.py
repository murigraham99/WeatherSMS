import requests
from twilio.rest import Client
import os

account_sid = "AC0754f4df27f93adbbbb11c5457024403"
auth_token = "e6c683399a526747f3026c7049b163e8"

# IP_KEY_1 = "baf6d53cf8caf9512c91a9e3ea16325d"
IP_KEY = os.environ.get("OWM_API_KEY")



test1 = 22.9473
test2 = 79.1923
lat = 44.4267674
lon = 26.10253839
params = {
    "lat": lat,
    "lon": lon,
    "appid": IP_KEY,
    "exclude": "current,minutely,daily,alerts"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=params)

print(response)
data = response.json()
hourly_id = []
will_rain = False
for hour in range(0, 12):
    ids = int(data["hourly"][hour]["weather"][0]["id"])
    hourly_id.append(ids)
    if ids < 700:
        will_rain = True


if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It is going to rain. Bring an umbrella! ⛱",
        from_="+14256003050",
        to="+40721266000"
    )
    print(message.sid)


