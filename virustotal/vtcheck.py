import requests
import environ
import os
env = environ.Env()
root = environ.Path(__file__) - 2

environ.Env.read_env(root('.env'))  
api_key = str(env('API_KEY'))

def check_hash_vt(hash):
    
    url = 'https://www.virustotal.com/vtapi/v2/file/report'
    params = {'apikey': api_key, 'resource': hash ,'allinfo':'1'}
    response = requests.get(url, params=params).json()
    print(response)
    response_code = int(response.get('response_code'))
    if (response_code == 0):
        return "Not_found"
    else:
        positives = int(response.get('positives'))
        total = int(response.get('total'))
        
        if ((positives / total) >= 0.75 ):
	        return "Malware"
        elif ((positives / total) >= 0 ) :
	        return "Benign"
        else :
            return "No_conclusion"

print(check_hash_vt("c00d90c50a5e05d270b796645d5f12dee94a31ca94b8ddc90c91af1f9e208850"))