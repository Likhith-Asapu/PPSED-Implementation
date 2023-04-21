import json
import os
from pseudo_random import *
from one_time_pad import number_to_binary
if os.path.isfile('user/r_key.json'):
    f = open('user/r_key.json')
    r_values = json.load(f)
else:
    r_values = {"current_seed":1,"r_value_file":{}}

if os.path.isfile('server/r_key.json'):
    f = open('server/r_key.json')
    r_values_server = json.load(f)
else:
    r_values_server = {"rvalues":{}}

def choose_r(r,file_name,t):
    for file_r in r_values["r_value_file"]:
        if file_r == file_name:
            return r_values["r_value_file"][file_r]
    number = r_values["current_seed"]
    r_values["r_value_file"][file_name] = number_to_binary(pseudo_random_function(r,number,t,t),t)
    # print(file_name)
    r_values_server["rvalues"][file_name[:-4]+".enc"] = number
    r = r_values["r_value_file"][file_name]
    with open('user/r_key.json','w') as f:
        json.dump(r_values,f)
    with open('server/r_key.json','w') as f:
        json.dump(r_values_server,f)

    return r