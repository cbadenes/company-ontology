import requests
import json
from IPython.core.display import display, HTML# An API Error Exception

class APIError(Exception):
    
    def __init__(self, status):
        self.status = status
        
    def __str__(self):
        return "APIError: status={}".format(self.status)
      
# Base URL for Spotlight API
base_url = "http://api.dbpedia-spotlight.org/en/annotate"# Parameters 

# 'text' - text to be annotated 
# 'confidence' -   confidence score for linking
params = {
    "text": "BASF SE is a German multinational chemical company and the largest chemical producer in the world.", 
    "confidence": 0.35}# Response content type
    
headers = {'accept': 'application/json'}# GET Request
res = requests.get(base_url, params=params, headers=headers)
if res.status_code != 200:
    # Something went wrong
    raise APIError(res.status_code)# Display the result as HTML in Jupyter Notebook
parsed = json.loads(res.text)
print(json.dumps(parsed, indent=4, sort_keys=True))