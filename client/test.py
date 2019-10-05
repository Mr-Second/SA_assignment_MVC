import os
import json
a = None
with open(os.getcwd()+'/a.json', 'r') as f:
    a = json.load(f)
print(a)
print(type(a))