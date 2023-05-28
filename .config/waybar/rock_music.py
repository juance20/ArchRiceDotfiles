import json
import os
try:
    with open("/tmp/rock_music","r") as file:
        data = json.load(file)
    
except FileNotFoundError:
    with open("/tmp/rock_music", "w") as file:
        data = {"playing":0}
        file.write(json.dumps(data, indent=4))

if data["playing"] == 0:
    with open("/tmp/rock_music", "w") as file:
        data = {"playing":1}
        file.write(json.dumps(data, indent=4))
    
    os.system("mpv https://www.youtube.com/playlist?list=PLggROXGdIiGYGxYD6YQd0JgLZCEeriboy --no-video --shuffle")
else:
    os.system("killall mpv")
    with open("/tmp/rock_music", "w") as file:
        data = {"playing":0}
        file.write(json.dumps(data, indent=4))
