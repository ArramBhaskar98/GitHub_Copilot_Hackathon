# GitHub_Copilot_Hackathon
GitHub Copilot Hackathon Contest for Weather Forecasting.

* Created a command line utility tool that accepts any city in the world and able to get the current and historical status of weather report.
* Inspired to participate in this GitHub Copilot Hackathon organized by TechGig. To know more, click [here](https://www.techgig.com/codegladiators/question/L0tUc2FLZFIyZit4L0F3bE9pOU5MbFN3b1VsR1FYZm55WjFHVW1TRUdyYkFCVENCUm1zMUxDaEpNZWRwSHdSSg==/1?msg_type=1)

## Steps to run the code.
* Clone this git repository into your local system.
* Create an account in [**Openweathermap**](https://openweathermap.org/) and generate an API Key under _My API keys_
* Copy the generated API Key and paste this in commonlibs.py script under getCityWeatherDetails function call.
* Run the weather_forecasting.py script by passing city name as command line argument. Note, City name can be in lower or upper case. Below is the sample call for your reference

Script Execution Steps : 
1. Goto bin directory of cloned repository.
2. Run the python script such as - python weather_forecasting.py "Hyderabad" . Here "Hyderabad" is the city name which is a command line argument to python script.
Example 1: python weather_forecasting.py "Hyderabad"
Example 2: python weather_forecasting.py "London"
