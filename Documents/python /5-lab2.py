x = ("Phnom Penh",  "Siem Reap", "Battambang")
y = (11.5564, 13.3622,  13.0957)
z = (104.9282, 103.8597, 103.2022)

t = zip(x, y, z)
for (x, y, z) in t:
    print(f"City: {x}, Latitude: {y}, Longitude: {z}")