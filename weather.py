my_lat = 40.71
my_lon = -74.00

# Watch how Python builds the string for you
magic_link = f"https://api.open-meteo.com/v1/forecast?latitude={my_lat}&longitude={my_lon}"

print(magic_link)