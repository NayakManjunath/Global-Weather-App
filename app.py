from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "73af25d0523a1ea15b3a4b0d076a4d8c"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def fetch_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        return response.json()
    return None

def parse_weather(data):
    return {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"],
    }

@app.route("/", methods=["GET", "POST"])
def home():
    weather = None

    if request.method == "POST":
        city = request.form.get("City")
        if city:
            data = fetch_weather(city)
            if data:
                weather = parse_weather(data)

    return render_template("index.html", weather=weather)

if __name__ == "__main__":
    app.run(debug=True)


# from flask import Flask, render_template, request

# app = Flask(__name__)
# import requests 

# API_KEY = "73af25d0523a1ea15b3a4b0d076a4d8c"
# BASE_URL = "https://api.openweather.org/data/2.5/weather"

# def fetch_weather (city):
#     params = {
#         "q" : city,
#         "appid": API_KEY,
#         "units": "metric"
#     }
#     response = requests.get(BASE_URL, params = params)
#     #https://api.openweather.org/data/2.5/weather?q={cityname}&=appid={API_KEY}
#     if response.status_code == 200:
#         return response.json()
#     else:
#         return None
    
# def parse_weather(data):
#     return {
#         "City" : data["name"],
#         "Temperature": data ["main"]["temp"],
#         "Description": data ["weather"] [0]["description"],
#         "Humidity": data ["main"] ["humidity"],
#         "Wind_speed": data ["wind"] ["speed"],

#     }

# # @app.route('/', methods=["GET", "POST"])
# # def home():
# #     weather = None
# #     if request.method == "POST":
# #         city = request.form.get(City)
# #         data = fetch_weather (city)
# #         if data:
# #             weather = parse_weather(data)

# #     return render_template("index.html", weather = weather)

# @app.route('/', methods=["GET", "POST"])
# def home():
#     weather = None

#     if request.method == "POST":
#         city = request.form.get("City")   # <-- use string
#         data = fetch_weather(city)
#         if data:
#             weather = parse_weather(data)

#     return render_template("index.html", weather=weather)

# # @app.route('/', methods=["GET", "POST"])
# # def home():
# #     weather = None
# #     if request.method == "POST":
# #         city = request.form.get("City")
# #         data = fetch_weather(city)
# #         if data:
# #             weather = parse_weather(data)

# #     return render_template("index.html", weather=weather)


# if __name__ == "__main__":
#     app.run(debug=True)