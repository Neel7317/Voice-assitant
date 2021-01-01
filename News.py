import requests
#key=5b1dc9ed9f8b4c7ebd942b7bb1037c6f
api_address="http://newsapi.org/v2/top-headlines?country=us&apiKey=5b1dc9ed9f8b4c7ebd942b7bb1037c6f"
json_data=requests.get(api_address).json()

ar=[]

def news():
    for i in range(3):
        ar.append("Number "+ str(i+1)+" "+ json_data["articles"][i]["title"] + ".")
        
    return ar


