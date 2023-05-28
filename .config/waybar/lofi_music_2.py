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
    printear = {"text": "󰎈", "tooltip": "Lo-Fi", "class":"stopped", "percentage":100}
    print(json.dumps(printear))

else:
    printear = {"text": "󰽴", "tooltip": "Lo-Fi", "class":"playing", "percentage":100}
    print(json.dumps(printear))
