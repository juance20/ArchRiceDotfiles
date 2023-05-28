import json
import os
try:
    with open("/tmp/lofi_music","r") as file:
        data = json.load(file)
    
except FileNotFoundError:
    with open("/tmp/lofi_music", "w") as file:
        data = {"playing":0}
        file.write(json.dumps(data, indent=4))

if data["playing"] == 0:
    with open("/tmp/lofi_music", "w") as file:
        data = {"playing":1}
        file.write(json.dumps(data, indent=4))
    
    os.system("mpv https://www.youtube.com/watch?v=jfKfPfyJRdk --no-video")
else:
    os.system("killall mpv")
    with open("/tmp/lofi_music", "w") as file:
        data = {"playing":0}
        file.write(json.dumps(data, indent=4))
