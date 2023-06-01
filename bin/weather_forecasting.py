import sys
from commonlibs import convertTimestamp, getCityWeatherDetails

name = sys.argv[1] if len(sys.argv) > 1 else None

if not name:
    print("Please Pass the City Name as Command Line Argument to script. Exit Program")
    exit(1)

# Calling the Weather API
response = getCityWeatherDetails(name)

# If we are interested in entire JSON response, comment all below lines (from if condition) and comment out the below line
# print("Response: ", response)
# return response

if response:
    res = response
    # print("Response Object : ", res)

    # It gives the weather description
    weather_description = res['weather'][0]['description']

    # It gives the temperature details
    humidity_details = res['main']['humidity']
    temperature_details = round(abs(res['main']['temp_max']-273), 2)

    # It gives the sunrise and sunset details
    sunrise_details = convertTimestamp(res['sys']['sunrise'])
    sunset_details = convertTimestamp(res['sys']['sunset'])

    print("Current Weather Status in {} is {}, Temperature is: {} degrees, Humidity is: {}, Sunrise Time is: {}, and Sunset Time is: {} ".format(name.title(), weather_description.title(), temperature_details, humidity_details, sunrise_details, sunset_details))
else:
    print("Error/Failed to Fetch the response: ", response)
