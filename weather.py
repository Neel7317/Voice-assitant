import requests
api_address="http://api.openweathermap.org/data/2.5/weather?q=surat&appid=30ba95391bd9d937c368f745a7a5e0e0"
json_data=requests.get(api_address).json()

def temp():
    tempratute=round(json_data["main"]["temp"]-273,1)
    return tempratute

def des():
    description=json_data["weather"][0]["description"]
    return description

