import requests
import json

response = requests.get('https://api.ipify.org?format=json')

if response.ok:
    data = {'text':response.json()['ip'],
            'tooltip':'Conected',
            'class':'connected',
            'percentage':100}

else:
    data = {'text':'NO','tooltip':'Disconnected','class':'disconnected','percentage':100}

print(json.dumps(data))
