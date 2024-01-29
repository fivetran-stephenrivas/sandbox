import os, json
import requests, requests.auth

# Find your API key and secret at 
# https://fivetran.com/docs/rest-api/getting-started#gettingstarted
api_key = os.environ['FIVETRAN_API_KEY']
api_secret = os.environ['FIVETRAN_API_SECRET']

# In your Fivetran Account, find your Destination Group ID
# on the Overview page for your destination
group_id = ''

webhook_receiver_url = ''

# REST API Request Constants
# Use this endpoint to setup webhooks for your entire Fivetran account
# fivetran_account_webhook_url = 'https://api.fivetran.com/v1/webhooks/account'
fivetran_group_webhook_url = f'https://api.fivetran.com/v1/webhooks/group/{group_id}'
request_auth = requests.auth.HTTPBasicAuth(api_key, api_secret)
request_body = {
    "url": webhook_receiver_url,
    # available events: https://fivetran.com/docs/rest-api/webhooks#events
    "events": [
        "sync_start",
        "sync_end"
    ]
}

# Main Program
try:
    response = requests.post(fivetran_group_webhook_url,
                             auth=request_auth,
                             json=request_body)

    #print response body as "pretty" JSON
    print(json.dumps(response.json(), indent=4))

    # If 4XX or 5XX response, raise Exception
    response.raise_for_status()
except requests.exceptions.HTTPError:
    raise
