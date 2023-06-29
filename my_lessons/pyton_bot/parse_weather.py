import requests
def parse_weather (city: str):
    api_key = 'Oebe025b8d93f180657fa5a4ccf33ba7'
    url='https://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city}'
    response = requests.get(url)

    return response.text

if __name__ == "__main__":
    city = input("Enter")
    weather = parse_weather(city)["main"]
    print(parse_weather("Kyiv")["main"])