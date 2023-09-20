from geopy.geocoders import Nominatim



geolocator = Nominatim(user_agent="Geolocator")

city_name = input("Enter City Name: ")

location = geolocator.geocode(city_name)



print(location)