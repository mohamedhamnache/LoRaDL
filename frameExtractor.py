
import requests
import json
import os 
username = "admin"
password = "lora@0309"
url = "http://localhost:8080/api"

EXP_FOLDER = 'exp/'
def connect():

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    data = '{ "password": "' + password + '", \n   "email": "' + username + '" \n }'

    response = requests.post(f"{url}/internal/login", headers=headers, data=data)
    r = json.loads(response.content.decode())
    try:
        return r["jwt"]
        # print(self.token)
    except:
        return None


def startGatewayFrameHandler(gatewayid):
    
    token = connect()
    
    if token :
        
        headers = {
            "Accept": "application/json",
            "Grpc-Metadata-Authorization": f"Bearer {token}",
        }


        with requests.get(f'{url}/gateways/{gatewayid}/frames', headers=headers, stream=True) as f:
            print(f)
            for l in f.iter_lines():
                if l:
                    decoded = l.decode()
                    trimmed = (
                        decoded.replace('\\"', '"')
                        .replace('"{', "{")
                        .replace('}"', "}")
                    )
                    data = json.loads(trimmed)
                    print(data)
    else:
        print('Authorization Required')

def startDeviceFrameHandler(devEUI):
    
    token = connect()
    
    if token :
        
        headers = {
            "Accept": "application/json",
            "Grpc-Metadata-Authorization": f"Bearer {token}",
        }


        with requests.get(f'{url}/devices/{devEUI}/frames', headers=headers, stream=True) as f:
            print(f)
            for l in f.iter_lines():
                if l:
                    decoded = l.decode()
                    trimmed = (
                        decoded.replace('\\"', '"')
                        .replace('"{', "{")
                        .replace('}"', "}")
                    )
                    data = json.loads(trimmed)
                    with open(f'{EXP_FOLDER}uplink.json', 'a') as outfile:
                        json.dump(data, outfile)
                    #print(data)
    else:
        print('Authorization Required')                  


#token = connect()
#print(token)

#startGatewayFrameHandler('3235313214003900')
startDeviceFrameHandler('deadbeefdead0064')