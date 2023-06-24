import subprocess
import os
r = subprocess.getoutput('pacmd list | grep "active port" | grep headphones')
if r == "":
   os.system("pacmd set-sink-port 0 analog-output-headphones")
else:
    os.system("pacmd set-sink-port 0 analog-output-lineout")
    
