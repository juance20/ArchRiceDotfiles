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
    printear = {"text": "󰌳", "tooltip": "Rock", "class":"stopped", "percentage":100}
    print(json.dumps(printear))

else:
    printear = {"text": "󰼄", "tooltip": "Rock", "class":"playing", "percentage":100}
    print(json.dumps(printear))
